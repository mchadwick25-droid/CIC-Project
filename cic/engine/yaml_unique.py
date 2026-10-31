"""YAML reading that refuses a repeated mapping key."""
from __future__ import annotations


def unique_key_loader():
    """A SafeLoader that refuses a mapping which repeats a key. The stock
    loader keeps the last value and says nothing, so a merge that wrote
    `language` twice in one row passed every check."""
    import yaml

    class UniqueKeyLoader(yaml.SafeLoader):
        def construct_mapping(self, node, deep=False):
            if isinstance(node, yaml.MappingNode):
                seen: set = set()
                for key_node, _ in node.value:
                    if key_node.tag == "tag:yaml.org,2002:merge":
                        continue
                    key = self.construct_object(key_node, deep=True)
                    try:
                        repeated = key in seen
                    except TypeError:
                        continue
                    if repeated:
                        raise yaml.constructor.ConstructorError(
                            "while constructing a mapping", node.start_mark,
                            f"repeated key {key!r}", key_node.start_mark)
                    seen.add(key)
            return super().construct_mapping(node, deep=deep)

    return UniqueKeyLoader


def load_unique(text: str):
    """yaml.safe_load that raises yaml.YAMLError on a repeated mapping key."""
    import yaml

    return yaml.load(text, Loader=unique_key_loader())  # noqa: S506 - a SafeLoader subclass
