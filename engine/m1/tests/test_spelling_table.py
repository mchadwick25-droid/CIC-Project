from engine.m1 import spelling_table as st


def test_normalize_maps_every_british_form_to_the_american_one():
    assert st.normalize("The colour of honour; they organised and travelled.") == "The color of honor; they organized and traveled."


def test_normalize_leaves_words_spelled_the_same_in_both_varieties():
    text = "advise exercise promise rigorous glamour analyses surprise"
    assert st.normalize(text) == text


def test_normalize_keeps_capitalization_and_the_lower_case_only_names():
    assert st.normalize("Centre DEFENCE Grey grey") == "Center DEFENSE Grey gray"


def test_normalize_is_idempotent_and_leaves_american_text_alone():
    once = st.normalize("neighbours' colour")
    assert st.normalize(once) == once
    assert st.normalize("neighbors' color") == "neighbors' color"


def test_american_gives_the_flagged_words_replacement():
    assert st.american("Saviours") == "Saviors"
    assert st.american("TRAVELLED") == "TRAVELED"
