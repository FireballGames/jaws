import os
import pygame

from .font import FontResources


PATH = os.path.abspath(os.path.join("res"))


def load_image(filename):
    image = pygame.image.load(os.path.join(PATH, 'img', filename)).convert()
    image.set_colorkey((255, 0, 255))
    return image


####################
# Title Screen Stuff

title_surfaces = dict()
title_surfaces['bg'] = load_image('titletext.png')

screen_size = 240

title_surfaces['newgame_gold'] = FontResources.gold.render("New Game", screen_size, 20, align='vcentre')
title_surfaces['continue_gold'] = FontResources.gold.render("Continue", screen_size, 20, align='vcentre')
title_surfaces['newgame_red'] = FontResources.gold.render("New Game", screen_size, 20, align='vcentre')
title_surfaces['continue_red'] = FontResources.gold.render("Continue", screen_size, 20, align='vcentre')

####################
# Pause Screen Stuff

# self.pause_spritedata = {}
# self.pause_spritedata['resume_on'] = gamefontred.RenderSentence("Resume Game", 640, 20, align='vcentre')
# self.pause_spritedata['resume_off'] = gamefontgold.RenderSentence("Resume Game", 640, 20, align='vcentre')
# self.pause_spritedata['reset_on'] = gamefontred.RenderSentence("Reset Level", 640, 20, align='vcentre')
# self.pause_spritedata['reset_off'] = gamefontgold.RenderSentence("Reset Level", 640, 20, align='vcentre')
# self.pause_spritedata['quit_on'] = gamefontred.RenderSentence("Quit Game", 640, 20, align='vcentre')
# self.pause_spritedata['quit_off'] = gamefontgold.RenderSentence("Quit Game", 640, 20, align='vcentre')

# for key in self.pause_spritedata.keys():
#     surf = self.pause_spritedata[key]
#     if type(surf) == type(True):
#         raise NotImplementedError("Surface render failed data: %s" % (key))

####################
# Cutscene Stuff

# Cutscene Surfaces
cutscene_surfaces = dict()

# Logo
cutscene_surfaces['team_chimera'] = load_image('team_chimera_5x.png')

# Intro cutscenes
cutscene_surfaces['intro_backdrop'] = load_image('intro_backdrop_7x.png')
cutscene_surfaces['intro_sprites'] = load_image('intro_sprites_7x.png')

intro_cutscene_sprites = dict()
intro_cutscene_sprites['water'] = [(7, 7, 56, 56), (63 + 7, 7, 56, 56), (119 + 14, 7, 56, 56),
                                            (175 + 21, 7, 56, 56), (231 + 28, 7, 56, 56)]
intro_cutscene_sprites['penguin'] = [(77, 70, 56, 63), (77, 140, 56, 63)]
intro_cutscene_sprites['man'] = [(7, 70, 56, 63), (7, 154, 56, 63)]
intro_cutscene_sprites['sub'] = [(119 + 21, 63, 126, 98)]

cutscene_surfaces['introtxt_001'] = FontResources.gold.render(
    "For years I had lived upon the glacier, sustaining myself by fishing through a hole in the ice.",
    600,
    60,
    align='vcentre'
)
cutscene_surfaces['introtxt_002'] = FontResources.gold.render(
    "The sea below the ice must have been a treasure trove of life, for I had caught many a tasty tuna, scrumptious salmon and heavenly haddock.",
    600,
    60,
    align='vcentre'
)
cutscene_surfaces['introtxt_003'] = FontResources.gold.render(
    "But fish were not all I caught: on my line I often hauled up strange artifacts and mysterious mechanisms from the icy depths.",
    600,
    60,
    align='vcentre'
)
cutscene_surfaces['introtxt_004'] = FontResources.gold.render(
    "I pondered over the origins of these strange objects. One day curiosity got the better of me.",
    600,
    60,
    align='vcentre'
)

cutscene_surfaces['introtxt_005'] = FontResources.gold.render(
    "I built a submarine that would take me under the ice. I had to get in there and find out where these treasures had come from.",
    600,
    60,
    align='vcentre'
)
cutscene_surfaces['introtxt_006'] = FontResources.gold.render(
    "Who can say what dangers I might encounter there? If my fate is to be a watery grave, then at least I`ll die knowing.",
    600,
    60,
    align='vcentre'
)

"""
        # In-between level cutscenes

        # cutscenesurfs['cut1_backdrop'] = pygame.image.load(os.path.join(mainpath,'data','gfx','intro_backdrop_7x.png')).convert()
        self.cutscenesurfs['cut1_backdrop'] = pygame.Surface((640, 480))
        self.cutscenesurfs['cut1_backdrop'].fill((255, 0, 255))
        self.cutscenesurfs['cut1_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut1_backdrop_sil'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'drfishhead_bg_sil.png')).convert()
        self.cutscenesurfs['cut1_backdrop_sil'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut1txt_001'] = gamefontgreen.RenderSentence(
            "Sir! We`ve detected a small vessel approaching the base.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_003'] = gamefontgreen.RenderSentence("He`ll discover everything.", 600, 60, align='vcentre')

        self.cutscenesurfs['cut1txt_004'] = gamefontred.RenderSentence(
            "What? Don`t bother me when I`m so close to finishing my work!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_005'] = gamefontred.RenderSentence(
            "Get out! Deal with the situation, and report back if there`s a real problem.", 600, 60, align='vcentre')

        self.cutscenesurfs['cut2_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'drfishhead_bg.png')).convert()
        self.cutscenesurfs['cut2_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut2txt_001'] = gamefontgreen.RenderSentence(
            "Sir! The vessel is getting closer! He`s almost at the perimeter of the base.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_003'] = gamefontgreen.RenderSentence("He`ll find out about project `Justice`.", 600, 60,
                                                                    align='vcentre')

        self.cutscenesurfs['cut2txt_004'] = gamefontred.RenderSentence(
            "So ... society outcasts me because of my hideous fish head and now they send someone to find me?", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut2txt_005'] = gamefontred.RenderSentence(
            "Never mind, they are too late to stop me! Project `Justice` is almost complete ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_006'] = gamefontred.RenderSentence(
            "... and for the world, `Justice` will be served ... Mwuuhahah!", 600, 60, align='vcentre')

        self.cutscenesurfs['cut3txt_001'] = gamefontgreen.RenderSentence("Sir! He`s breached the perimeter!", 600, 60,
                                                                    align='vcentre')
        self.cutscenesurfs['cut3txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_003'] = gamefontgreen.RenderSentence("He`ll be outside the base in minutes!", 600, 60,
                                                                    align='vcentre')

        self.cutscenesurfs['cut3txt_004'] = gamefontred.RenderSentence(
            "No ... it`s too close to the end now to run away. `Justice` is almost complete.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_005'] = gamefontred.RenderSentence(
            "When I lived in the world above the waves, I was not good enough for them.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_006'] = gamefontred.RenderSentence(
            "Everywhere I went ... bars, restaurants, the subway, I was told:", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_007'] = gamefontgold.RenderSentence('"We can`t let you in here!"', 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_008'] = gamefontred.RenderSentence("They told me I had fish odour.", 600, 60,
                                                                  align='vcentre')
        self.cutscenesurfs['cut3txt_009'] = gamefontred.RenderSentence(
            "Well now I will prove my worth to them! I`ve come too far to be stopped.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_010'] = gamefontred.RenderSentence("There`s only one thing left to do ...", 600, 60,
                                                                  align='vcentre')

        self.cutscenesurfs['cut3txt_011'] = gamefontgreen.RenderSentence("Sir! No, not that ... it`s ... it`s too dangerous!",
                                                                    600, 60, align='vcentre')

        self.cutscenesurfs['cut3_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'roboshark_bg.png')).convert()
        self.cutscenesurfs['cut3_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut3txt_012'] = gamefontred.RenderSentence("Silence! Release the Roboshark!", 600, 60,
                                                                  align='vcentre')

        self.cutscenesurfs['cut4_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'cutscenefinal.png')).convert()
        self.cutscenesurfs['cut4_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut4_backdrop2'] = pygame.Surface((640, 480))
        self.cutscenesurfs['cut4_backdrop2'].fill((255, 0, 255))
        self.cutscenesurfs['cut4_backdrop2'].set_colorkey((255, 0, 255))
        self.cutscenesurfs['cut4_backdrop2'].blit(self.backdrop, (0, 0))

        self.cutscenesurfs['cut4txt_001'] = gamefontred.RenderSentence(
            "How did you get in here? You weren`t supposed to come in here!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_002'] = gamefontred.RenderSentence("My secrets ... all ruined ... project `Justice` ...",
                                                                  600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_003'] = gamefontgold.RenderSentence("Wow! this is amazing! You mean you live down here?",
                                                                   600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_004'] = gamefontred.RenderSentence("Ahh ... yes I do ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_005'] = gamefontgold.RenderSentence(
            "I`ve never seen anything so cool. I mean, an underwater base is about as cool as it gets.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_006'] = gamefontred.RenderSentence(
            "Well, yes ... hold on! You mean you`re not here to steal my secret recipe?", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_007'] = gamefontgold.RenderSentence("Ahhh, nope.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_008'] = gamefontred.RenderSentence(
            "Then project `Justice` is safe! At last the world will taste my delicious oyster sauce.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_009'] = gamefontred.RenderSentence(
            "I`ve been working down here on the perfect recipe for months. I`m going to call my delicous oyster sauce `Justice` and serve it to the whole world.",
            600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_010'] = gamefontred.RenderSentence(
            "I wanted to show the world that my culinary talents can make up for my hideous personal appearence.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_011'] = gamefontgold.RenderSentence("What do you mean?", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_012'] = gamefontred.RenderSentence(
            "My hideous appearance. I have the body of a man and the head of a fish. Haven`t you noticed?", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_013'] = gamefontgold.RenderSentence(
            "Ah, no, I didn`t really see that ... now that you mention it ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_014'] = gamefontred.RenderSentence("Would you like to try some `Justice`?", 600, 60,
                                                                  align='vcentre')
        self.cutscenesurfs['cut4txt_015'] = gamefontgold.RenderSentence(
            "Sure, that would be great. I`ve got a couple of pounds of squid that I picked up on the way here. I`m starved!",
            600, 60, align='vcentre')

        self.cutscenesurfs['cut4txt_016'] = gamefontgold.RenderSentence(
            "Congratulations! Game Complete! Best Friends Forever ...", 600, 60, align='vcentre')

        for key in self.cutscenesurfs.keys():
            surf = self.cutscenesurfs[key]
            if type(surf) == type(True):
                raise NotImplementedError("Surface render failed cutscene data: %s" % (key))

"""

###########################
# Actual cutscene content

"""
introcutscene_data = [
    [
        ['intro_backdrop',['introtxt_001']]
    ],
    'none',
    'titlescene',
    []
]
introcutscene_data = [
    [
        ['intro_backdrop',['introtxt_001','introtxt_002','introtxt_003','introtxt_004']],
        ['intro_backdrop',['introtxt_005','introtxt_006']]
    ],
    'wind_effect',
    'maingame',
    [True, "level_explore_001"]
]
"""
intro_cutscene = [
    [
        ['intro_backdrop', ['introtxt_001', 'introtxt_002', 'introtxt_003', 'introtxt_004']],
        ['intro_backdrop', ['introtxt_005', 'introtxt_006']]
    ],
    'wind_effect',
    'title',
    []
]

"""
self.cutscene1_data = [[['cut1_backdrop', ['cut1txt_001', 'cut1txt_002', 'cut1txt_003']], \
                   ['cut1_backdrop_sil', ['cut1txt_004', 'cut1txt_005']]], 'none', 'maingame',
                  [True, "level_sharksandmines_004"]]

self.cutscene2_data = [[['cut1_backdrop', ['cut2txt_001', 'cut2txt_002', 'cut2txt_003']], \
                   ['cut2_backdrop', ['cut2txt_004', 'cut2txt_005', 'cut2txt_006']]], 'none', 'maingame',
                  [True, "level_magnet_006"]]

self.cutscene3_data = [[['cut1_backdrop', ['cut3txt_001', 'cut3txt_002', 'cut3txt_003']], \
                   ['cut2_backdrop',
                    ['cut3txt_004', 'cut3txt_005', 'cut3txt_006', 'cut3txt_007', 'cut3txt_008', 'cut3txt_009',
                     'cut3txt_010', 'cut3txt_011']], \
                   ['cut3_backdrop', ['cut3txt_012']]], 'none', 'maingame', [True, "level_sharkmagnet_008"]]

self.cutscene5_data = [[['cut4_backdrop2', ['cut4txt_016']]], 'pamgaea', 'titlescene', []]

self.cutscene4_data = [[['cut4_backdrop',
                    ['cut4txt_001', 'cut4txt_002', 'cut4txt_003', 'cut4txt_004', 'cut4txt_005', 'cut4txt_006',
                     'cut4txt_007', 'cut4txt_008', 'cut4txt_009', 'cut4txt_010', 'cut4txt_011', 'cut4txt_012',
                     'cut4txt_013', 'cut4txt_014', 'cut4txt_015']]], 'none', 'cutscene5', self.cutscene5_data]
"""

"""
logocutscene_data = [
    [
        [
            'team_chimera',
            []
        ]
    ],
    'none',
    'titlescene',
    []
]

logocutscene_data = [
    [
        [
            'team_chimera',
            []
        ]
    ],
    'none',
    'maingame',
    [
        True,
        "level_explore_001"
    ]
]
"""
logo_cutscene = [
    [
        ['team_chimera', []],
    ],
    None,
    'intro',
    intro_cutscene
]

