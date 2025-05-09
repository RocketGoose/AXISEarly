from industry import IndustryPrimaryExtractive, TileLocationChecks


industry = IndustryPrimaryExtractive(
    id="bauxite_mine",
    prod_cargo_types_with_multipliers=[("AORE", 20)],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="85",
    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
    location_checks=dict(require_cluster=[90, 4]),
    prospect_chance="0.75",
    name="string(STR_IND_BAUXITE_MINE)",
    nearby_station_name="string(STR_STATION_BAUXITE)",
    fund_cost_multiplier="200",
    pollution_and_squalor_factor=1,
    intro_year=1860,
)


industry.economy_variations["STEELTOWN"].enabled = True


# 2 tiles for this industry: pit outer tile cannot be on slopes; pit inner tiles and processor tiles can be
# cases for both tiles ensure that tiles can only be built at same height as north tile
industry.add_tile(id='bauxite_mine_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='bauxite_mine_tile_2',
                  animation_length=56,
                  animation_looping=True,
                  animation_speed=4,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  foundations='return CB_RESULT_NO_FOUNDATIONS',  # might not be needed, cargo-culted from previous code, didn't test; may be needed to stop rear foundations showing in some cases?
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='empty'
)
spriteset_animated_dozer = industry.add_spriteset(
    sprites=[(440, 90, 64, 31, -31, 0), (510, 90, 64, 31, -31, 0), (580, 90, 64, 31, -31, 0),
             (650, 90, 64, 31, -31, 0), (720, 90, 64, 31, -31, 0), (790, 90, 64, 31, -31, 0),
             (790, 90, 64, 31, -31, 0), (720, 90, 64, 31, -31, 0), (650, 90, 64, 31, -31, 0),
             (580, 90, 64, 31, -31, 0), (510, 90, 64, 31, -31, 0), (440, 90, 64, 31, -31, 0)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame < 36) ? (animation_frame % 12) : 0',
)
spriteset_ground_animated_tile = industry.add_spriteset(
    type='empty',
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 90, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 90, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_4 = industry.add_spriteset(
    sprites=[(150, 90, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_5 = industry.add_spriteset(
    sprites=[(220, 90, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_6 = industry.add_spriteset(
    sprites=[(290, 90, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_7 = industry.add_spriteset(
    sprites=[(10, 50, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_8 = industry.add_spriteset(
    sprites=[(80, 50, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_10 = industry.add_spriteset(
    sprites=[(150, 50, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_11 = industry.add_spriteset(
    sprites=[(220, 50, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_12 = industry.add_spriteset(
    sprites=[(290, 50, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_19 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_20 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_22 = industry.add_spriteset(
    sprites=[(150, 10, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_23 = industry.add_spriteset(
    sprites=[(220, 10, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_24 = industry.add_spriteset(
    sprites=[(290, 10, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_pile = industry.add_spriteset(
    sprites=[(360, 50, 64, 31, -63, -16)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_crane_1 = industry.add_spriteset(
    sprites=[(440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55), (510, 10, 64, 71, -48, -55),
             (580, 10, 64, 71, -48, -55), (650, 10, 64, 71, -48, -55), (650, 10, 64, 71, -48, -55),
             (650, 10, 64, 71, -48, -55), (580, 10, 64, 71, -48, -55), (510, 10, 64, 71, -48, -55),
             (440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame > 32) ? (animation_frame % 12) : 0',
)
spriteset_pit_conveyor_0 = industry.add_spriteset(
    sprites=[(10, 130, 64, 64, -31, -22)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_pit_conveyor_1 = industry.add_spriteset(
    sprites=[(80, 130, 64, 64, -31, -22)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_pit_conveyor_2 = industry.add_spriteset(
    sprites=[(150, 130, 64, 64, -31, -22)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_pit_conveyor_3 = industry.add_spriteset(
    sprites=[(220, 130, 64, 64, -31, -22)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_pit_conveyor_4 = industry.add_spriteset(
    sprites=[(290, 130, 64, 64, -31, -22)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_39 = industry.add_spriteset(
    sprites=[(870, 10, 64, 31, -31, 0)],
)
spriteset_40 = industry.add_spriteset(
    sprites=[(940, 10, 64, 31, -31, 0)],
)
spriteset_41 = industry.add_spriteset(
    sprites=[(1010, 10, 64, 34, -31, -3)],
)
spriteset_silo = industry.add_spriteset(
    sprites=[(870, 50, 64, 64, -31, -35)],
)
spriteset_conveyor_2 = industry.add_spriteset(
    sprites=[(940, 50, 64, 64, -31, -35)],
)
spriteset_crusher = industry.add_spriteset(
    sprites=[(1010, 50, 64, 64, -31, -33)],
)

industry.add_spritelayout(
    id='bauxite_mine_spritelayout_1',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_1,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_2',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_2,
    building_sprites=[spriteset_pit_conveyor_0],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_4',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_4,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_5',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_5,
    building_sprites=[spriteset_crane_1, spriteset_pile],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_6',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_6,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_7',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_7,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_8',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_8,
    building_sprites=[spriteset_animated_dozer],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_10',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_10,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_11',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_11,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_12',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_12,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_19',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_19,
    building_sprites=[],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_20',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_20,
    building_sprites=[spriteset_pit_conveyor_1],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_22',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_22,
    building_sprites=[spriteset_pit_conveyor_2],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_23',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_23,
    building_sprites=[spriteset_pit_conveyor_3],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_24',
    ground_sprite=spriteset_ground_animated_tile,
    ground_overlay=spriteset_24,
    building_sprites=[spriteset_pit_conveyor_4],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_39',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_39,
    building_sprites=[spriteset_silo],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_40',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_40,
    building_sprites=[spriteset_conveyor_2],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id='bauxite_mine_spritelayout_41',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_41,
    building_sprites=[spriteset_crusher],
    terrain_aware_ground=True,
)


industry.add_industry_layout(
    id='bauxite_mine_layout_1',
    layout=[(0, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_24'),
            (0, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_12'),
            (0, 3, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_6'),
            (1, 0, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_41'),
            (1, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_23'),
            (1, 2, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_11'),
            (1, 3, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_5'),
            (2, 0, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_40'),
            (2, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_22'),
            (2, 2, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_10'),
            (2, 3, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_4'),
            (3, 0, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_39'),
            (3, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_20'),
            (3, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_8'),
            (3, 3, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_2'),
            (4, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_19'),
            (4, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_7'),
            (4, 3, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_1'),
            ]
)

industry.add_industry_layout(
    id='bauxite_mine_layout_2',
    layout=[(0, 0, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_24'),
            (0, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_12'),
            (0, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_6'),
            (1, 0, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_23'),
            (1, 1, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_11'),
            (1, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_5'),
            (1, 3, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_41'),
            (2, 0, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_22'),
            (2, 1, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_10'),
            (2, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_4'),
            (2, 3, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_40'),
            (3, 0, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_20'),
            (3, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_8'),
            (3, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_2'),
            (3, 3, 'bauxite_mine_tile_1', 'bauxite_mine_spritelayout_39'),
            (4, 0, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_19'),
            (4, 1, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_7'),
            (4, 2, 'bauxite_mine_tile_2', 'bauxite_mine_spritelayout_1'),
            ]
)
