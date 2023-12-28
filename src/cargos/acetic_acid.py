from cargo import Cargo

cargo = Cargo(
    id="acetic_acid",
    type_name="string(STR_CARGO_NAME_ACETIC_ACID)",
    unit_name="string(STR_CARGO_NAME_ACETIC_ACID)",
    type_abbreviation="string(STR_CID_ACETIC_ACID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.5",  # extra realism, per forum suggestion Nov 2017
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_HAZARDOUS)",
    cargo_label="ACET",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_ACETIC_ACID)",
    penalty_lowerbound="24",
    single_penalty_length="48",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(15, 6),
    sprites_complete=True,
)