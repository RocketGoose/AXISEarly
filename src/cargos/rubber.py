from cargo import Cargo

cargo = Cargo(
    id="rubber",
    type_name="TTD_STR_CARGO_PLURAL_RUBBER",
    unit_name="TTD_STR_CARGO_SINGULAR_RUBBER",
    type_abbreviation="string(STR_CID_RUBBER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="RUBR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="TTD_STR_QUANTITY_RUBBER",
    penalty_lowerbound="10",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=110,
    icon_indices=(2, 2),
    sprites_complete=True,
)
