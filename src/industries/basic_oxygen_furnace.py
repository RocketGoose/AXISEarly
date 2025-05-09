from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="basic_oxygen_furnace",
    accept_cargos_with_input_ratios=[
        ("IRON", 4),
        ("FECR", 2),
        ("QLME", 1),
        ("O2__", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("STCB", 3), ("STAL", 3), ("SLAG", 2)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="49",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["blast_furnace"], 72],
        same_type_distance=72,
    ),
    name="string(STR_IND_BASIC_OXYGEN_FURNACE)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="160",
    pollution_and_squalor_factor=2,
    intro_year=1952,
)

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "0"  # do not build during gameplay

industry.economy_variations["BASIC_TROPIC"].enabled = True
industry.economy_variations[
    "BASIC_TROPIC"
].prob_in_game = "0"  # do not build during gameplay
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("IRON", 3),
    ("SCMT", 3),  
    ("QLME", 1),
    ("RAMT", 1),  
]
industry.economy_variations["BASIC_TROPIC"].prod_cargo_types_with_output_ratios = [
    ("STEL", 6),
    ("SLAG", 2),
]

industry.add_tile(
    id="basic_oxygen_furnace_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="hard_standing_dirt",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
# unused
spriteset_manganese_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_furnace = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_caster = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_metal_3 = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_metal_4 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -90)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=61,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=4,
    yoffset=1,
    zoffset=93,
)

industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_manganese_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_manganese_1],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_air_plant",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_air_plant],
    smoke_sprites=[sprite_smoke_2],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_furnace",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_furnace],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_caster",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_caster],
    smoke_sprites=[sprite_smoke_1],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_2],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_3],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_4],

)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_shed",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed],

)

# min 6x4 or 5x5 as there are lots of output cargos
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_1",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (0, 4, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (0, 5, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            1,
            5,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            2,
            5,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_manganese_1",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_2",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            3,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            3,
            5,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_2",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (0, 4, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_2",
        ),
        (
            3,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (4, 0, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (4, 1, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (
            4,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_manganese_1",
        ),
        (
            4,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            4,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_3",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_2",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            3,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            4,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (4, 1, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (4, 2, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (
            4,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            4,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_manganese_1",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_4",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_caster",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_manganese_1",
        ),
        (
            4,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            4,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            4,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_empty",
        ),
        (4, 3, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
        (
            5,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_4",
        ),
        (
            5,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_2",
        ),
        (
            5,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_3",
        ),
        (5, 3, "basic_oxygen_furnace_tile_1", "basic_oxygen_furnace_spritelayout_shed"),
    ],
)
