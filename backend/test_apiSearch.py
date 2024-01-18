from apiSearch import broadSearch, narrowSearch, exactSearch


def test_broadsearch():
    # This tests the broad search with a family search
    assert broadSearch("search", 0, "Star Trek") == {
        "@total": "11",
        "@termsofuse": "https://boardgamegeek.com/xmlapi/termsofuse",
        "item": [
            {
                "@type": "rpg",
                "@id": "26696",
                "name": {
                    "@type": "primary",
                    "@value": "Alea:Est Il Gioco di Ruolo di Star Trek",
                },
            },
            {
                "@type": "rpg",
                "@id": "2447",
                "name": {
                    "@type": "primary",
                    "@value": "Enterprise - Role Play Game in Star Trek",
                },
            },
            {
                "@type": "rpg",
                "@id": "51858",
                "name": {
                    "@type": "primary",
                    "@value": "The Fantasy Guide to Star Trek",
                },
            },
            {
                "@type": "rpg",
                "@id": "37049",
                "name": {"@type": "primary", "@value": "Star Trek Adventures"},
            },
            {
                "@type": "rpg",
                "@id": "1481",
                "name": {"@type": "primary", "@value": "Star Trek Roleplaying Game"},
            },
            {
                "@type": "rpg",
                "@id": "706",
                "name": {
                    "@type": "primary",
                    "@value": "Star Trek:  The Next Generation Roleplaying Game",
                },
            },
            {
                "@type": "rpg",
                "@id": "705",
                "name": {
                    "@type": "primary",
                    "@value": "Star Trek:  The Original Series Roleplaying Game",
                },
            },
            {
                "@type": "rpg",
                "@id": "1622",
                "name": {
                    "@type": "primary",
                    "@value": "Star Trek: Adventure Gaming in the Final Frontier",
                },
            },
            {
                "@type": "rpg",
                "@id": "41468",
                "name": {"@type": "primary", "@value": "Star Trek: Alpha Quadrant"},
            },
            {
                "@type": "rpg",
                "@id": "707",
                "name": {
                    "@type": "primary",
                    "@value": "Star Trek: Deep Space Nine Roleplaying Game",
                },
            },
            {
                "@type": "rpg",
                "@id": "353",
                "name": {
                    "@type": "primary",
                    "@value": "Star Trek: The Role Playing Game (FASA)",
                },
            },
        ],
    }


def test_narrowSearch():
    assert narrowSearch("family", 0, 37049) == {
        "@type": "rpg",
        "@id": "37049",
        "thumbnail": "https://cf.geekdo-images.com/UwlDjgsfHcG2ZEDMEJvVRQ__thumb/img/CW6yHYKZrsU2T7Lk5hrZh7Z619E=/fit-in/200x150/filters:strip_icc()/pic3687599.png",
        "image": "https://cf.geekdo-images.com/UwlDjgsfHcG2ZEDMEJvVRQ__original/img/0Q5Ec3hvRfNMMVlPkqBF6-jyEZQ=/0x0/filters:format(png)/pic3687599.png",
        "name": [
            {"@type": "primary", "@sortindex": "1", "@value": "Star Trek Adventures"},
            {
                "@type": "alternate",
                "@sortindex": "1",
                "@value": "Звездный путь. Приключения в космосе",
            },
        ],
        "description": "Description from the publisher:&#10;&#10;Star Trek Adventures uses the Modiphius 2d20 game system (Mutant Chronicles, Infinity, Conan, John Carter of Mars) designed by Jay Little (Star Wars: Edge of the Empire, X-Wing Miniatures Game). Modiphius is also sculpting an accompanying Star Trek miniature figure line, the first to be produced in seventeen years. Resin and metal 32mm-scale hobby figures will feature classic Star Trek characters and crews, boarding parties, and away teams. Geomorphic tile maps of burning Federation ships, mysterious colonies and embattled Klingon cruisers will set the scene for dramatic new voyages in the Final Frontier.&#10; Under license by CBS Consumer Products, Star Trek Adventures is slated for a mid-2017 release and the playtest crews will be listed in the Star Trek Adventures book manifest.&#10;&#10;",
        "link": [
            {
                "@type": "rpg",
                "@id": "386783",
                "@value": "STA TOS 2: Abyss Station",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386782",
                "@value": "STA TOS 1: Adrift",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "285191",
                "@value": "Alpha Quadrant Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "378811",
                "@value": "Mission Briefs 010: Ancient Civilizations",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "272273",
                "@value": "Andromeda: A Mission Compendium for Star Trek Adventures",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "341203",
                "@value": "Mission Briefs 003: Anomalies",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "330459",
                "@value": "Another Roll of the Dice",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386796",
                "@value": "STA TNG 8: The Assessor Gambit",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386785",
                "@value": "STA TOS 4: Bacchus' Irresistible Call",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "323837",
                "@value": "Back to Reality",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "254520",
                "@value": "Beta Quadrant Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "369343",
                "@value": "Better Days",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "235854",
                "@value": "Borg Cube Collector's Edition Box Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "341204",
                "@value": "The Burning",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "266036",
                "@value": "Call Back Yesterday",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "403635",
                "@value": "Children of the Wolf",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "254521",
                "@value": "The Command Division Supplemental Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386792",
                "@value": "STA TNG 4: Convoy SE-119",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "401386",
                "@value": "Mission Briefs 013: Dangers in Space",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "291891",
                "@value": "Dark Mirror",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386789",
                "@value": "STA TNG 1: Decision Point",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "291454",
                "@value": "Deep Space 24",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "261888",
                "@value": "Deep Space Nine Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "304901",
                "@value": "Delta Quadrant Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "338347",
                "@value": "Mission Briefs 002: Disasters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386797",
                "@value": "STA TNG 9: The Displaced",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386790",
                "@value": "STA TNG 2: Doomed to Repeat the Past",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "380920",
                "@value": "Eight Layers Deep",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "254101",
                "@value": "Ends and Means",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "316738",
                "@value": "Enterprise Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386791",
                "@value": "STA TNG 3: Fading Sun",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "367841",
                "@value": "Mission Briefs 007: First Contacts",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "313792",
                "@value": "A Forest Apart",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386784",
                "@value": "STA TOS 3: Fury of the Hive",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "299092",
                "@value": "Gamma Quadrant Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "273161",
                "@value": "The Gravity of the Crime",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "338348",
                "@value": "Mission Briefs 001: Growing Pains",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "315964",
                "@value": "Hard Rock Catastrophe",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "408325",
                "@value": "A House by Any Other Name",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "272274",
                "@value": "Hurricane: A Mission Compendium for Star Trek Adventures",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "316986",
                "@value": "Iconic Villains: Non-Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "348527",
                "@value": "IDW Year Five Tie-In",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "335335",
                "@value": "Ignitrix's Hidden Library",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "376980",
                "@value": "Incident at Kraav III",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "364750",
                "@value": "The Keyhole of Eternity",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "313740",
                "@value": "The Klingon Empire",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "314519",
                "@value": "Kobayashi Maru",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "391267",
                "@value": "Mission Briefs 011: Lower Decks",
                "@inbound": "true",
            },
            {"@type": "rpg", "@id": "385979", "@value": "Lurkers", "@inbound": "true"},
            {
                "@type": "rpg",
                "@id": "375570",
                "@value": "Mission Briefs 009: Mysteries",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "373241",
                "@value": "Native Soil",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "313793",
                "@value": "Nest in the Dark",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "244246",
                "@value": "The Next Generation Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "264713",
                "@value": "The Operations Division Supplemental Rulebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "244245",
                "@value": "The Original Series Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "272276",
                "@value": "Pandora's Box: A Mission Compendium for Star Trek Adventures",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "398959",
                "@value": "A Piece of Qo'noS",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "325843",
                "@value": "The Prize",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "291892",
                "@value": "Psi Shift",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "363713",
                "@value": "Mission Briefs 006: Psychic Incursions",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386788",
                "@value": "STA TOS 7: Punishment & Crime",
                "@inbound": "true",
            },
            {"@type": "rpg", "@id": "261260", "@value": "Remnants", "@inbound": "true"},
            {
                "@type": "rpg",
                "@id": "272277",
                "@value": "Rig for Red: An Unofficial Stand-Alone Mission for 2373",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "328263",
                "@value": "The Romulan Star Empire",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "273383",
                "@value": "The Sciences Division Supplemental Rulebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "347202",
                "@value": "Shackleton Expanse Campaign Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386794",
                "@value": "STA TNG 6: Signals",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386787",
                "@value": "STA TOS 6: Simplicity",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "382866",
                "@value": "The Sleeping Beast",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "371503",
                "@value": "Mission Briefs 008: Spacewrecks",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "253429",
                "@value": "A Star Beyond the Stars",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "204868",
                "@value": "Star Trek Adventures Core Book",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "355450",
                "@value": "Star Trek Adventures Gamemaster's Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "235881",
                "@value": "Star Trek Adventures GM Screen",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "355449",
                "@value": "Star Trek Adventures Player's Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "236598",
                "@value": "Star Trek Adventures Quickstart Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "235855",
                "@value": "Star Trek Adventures Roleplaying Dice Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "363269",
                "@value": "Star Trek Adventures Rules Digest",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "395320",
                "@value": "Star Trek Adventures: Captain's Log Solo Roleplaying Game",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "334453",
                "@value": "Star Trek Adventures: Klingon Quickstart",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "258426",
                "@value": "Star Trek Adventures: Starter Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "315963",
                "@value": "Star Trek Adventures: The Next Generation Klingon Tile Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "360860",
                "@value": "Star Trek: Discovery (2256-2258) Campaign Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "359294",
                "@value": "Star Trek: Discovery Season 1 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "360850",
                "@value": "Star Trek: Discovery Season 2 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "363280",
                "@value": "Star Trek: Discovery Season 3 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "396552",
                "@value": "Star Trek: Lower Decks Campaign Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "385981",
                "@value": "Star Trek: Lower Decks Season 1 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "388006",
                "@value": "Star Trek: Lower Decks Season 2 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "366611",
                "@value": "Star Trek: Picard Season 1 Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "401257",
                "@value": "Star Trek: The Animated Series Supplemental Guide",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "283340",
                "@value": "Star Trek: The Next Generation Starfleet Tile Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386799",
                "@value": "Starbase 364 and the Shackleton Expanse",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "359574",
                "@value": "Mission Briefs 005: Starbase Adventures",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "396850",
                "@value": "Mission Briefs 012: Starfleet Academy",
                "@inbound": "true",
            },
            {"@type": "rpg", "@id": "344507", "@value": "Starlogs", "@inbound": "true"},
            {
                "@type": "rpg",
                "@id": "294495",
                "@value": "Stolen Liberty",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "361916",
                "@value": "Storms of Kiselia",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "295117",
                "@value": "Strange New Worlds: Mission Compendium Vol. 2",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "235569",
                "@value": "These Are the Voyages: Mission Compendium Vol. 1",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "355451",
                "@value": "Mission Briefs 004: Trade Ledgers",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "276935",
                "@value": "Tribble (Playable Race)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "349761",
                "@value": "Tricorder Collector's Edition Box Set",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "272661",
                "@value": "Trouble on Omned III",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386793",
                "@value": "STA TNG 5: Tug of War",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "365619",
                "@value": "Unforeseen Consequences",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "357826",
                "@value": "Upsetting the Balance",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "371696",
                "@value": "Utopia Planitia Starfleet Sourcebook",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "295691",
                "@value": "Voyager Player Characters",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386795",
                "@value": "STA TNG 7: We Are the Stars that Sing With Our Life",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "386786",
                "@value": "STA TOS 5: We Came Forth to Contemplate the Stars",
                "@inbound": "true",
            },
            {"@type": "rpgfamily", "@id": "352", "@value": "Star Trek"},
            {"@type": "rpgsystem", "@id": "34087", "@value": "2d20 System"},
            {
                "@type": "rpg",
                "@id": "2274",
                "@value": "Star Trek Universe",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "74804",
                "@value": "Mission Briefs",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "79689",
                "@value": "Star Trek Adventures Living Campaign (TNG 2371)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "79688",
                "@value": "Star Trek Adventures Living Campaign (TOS 2269)",
                "@inbound": "true",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2101",
                "@value": "Attribute/Stat Based (STR, CON, PER, etc)",
            },
            {"@type": "rpgmechanic", "@id": "2088", "@value": "Dice (Primarily d20)"},
            {
                "@type": "rpgmechanic",
                "@id": "2124",
                "@value": "Lifepath Character Generation (Character starts at birth)",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2138",
                "@value": "Progression Tree (Skills, professions, magic abilities, etc.)",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2094",
                "@value": "Skill Based (buy or gain skills)",
            },
            {
                "@type": "rpg",
                "@id": "212230",
                "@value": "Alarums & Excursions (Issue 493 - Nov 2016)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "290151",
                "@value": "Alarums & Excursions (Issue 527 - Oct 2019)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "305807",
                "@value": "Casus Belli (v4, Issue 30 - Jul/Aug 2019)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "333470",
                "@value": "The Killing Fields (Issue 7 - Mar 2021)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "254354",
                "@value": "Mephisto (Issue 68 - Jun/Jul 2018)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "267610",
                "@value": "Mephisto (Issue 69 - Jan/Feb 2019)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "222875",
                "@value": "Modiphia (Issue #1 - Spring 2017)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "233545",
                "@value": "Modiphia (Issue #2 - Summer 2017)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "245849",
                "@value": "Modiphia (Issue #3 - Winter 2017/2018)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "319000",
                "@value": "Tabletop Gaming - Dungeon Master's Guide to Roleplaying, Volume One",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "331270",
                "@value": "Tabletop Gaming (Issue 12 - Oct/Nov 2017)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "331291",
                "@value": "Tabletop Gaming (Issue 19 - Jun 2018)",
                "@inbound": "true",
            },
            {
                "@type": "rpg",
                "@id": "331248",
                "@value": "Tabletop Gaming (Issue 48 - Nov 2020)",
                "@inbound": "true",
            },
        ],
    }


def test_exactSearch():
    assert exactSearch(386784, "STA TOS 3: Fury of the Hive", "rpgitem") == {
        "@type": "rpgitem",
        "@id": "386784",
        "thumbnail": "https://cf.geekdo-images.com/2x1kNY5aj6rHggWDBoTiVQ__thumb/img/KpyBtkoyw_MHohFoa6pQdrTNt0A=/fit-in/200x150/filters:strip_icc()/pic7481347.jpg",
        "image": "https://cf.geekdo-images.com/2x1kNY5aj6rHggWDBoTiVQ__original/img/ln26xloHajwY8-J856pm7ntFlQs=/0x0/filters:format(jpeg)/pic7481347.jpg",
        "name": {"@type": "primary", "@sortindex": "1", "@value": "Fury of the Hive"},
        "link": [
            {"@type": "rpg", "@id": "37049", "@value": "Star Trek Adventures"},
            {
                "@type": "rpggenre",
                "@id": "162",
                "@value": "Science Fiction (Space Opera)",
            },
            {"@type": "rpgsetting", "@id": "2274", "@value": "Star Trek Universe"},
            {
                "@type": "rpgseries",
                "@id": "79688",
                "@value": "Star Trek Adventures Living Campaign (TOS 2269)",
            },
            {
                "@type": "rpgcategory",
                "@id": "2084",
                "@value": "Scenario / Adventure / Module",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2101",
                "@value": "Attribute/Stat Based (STR, CON, PER, etc)",
            },
            {"@type": "rpgmechanic", "@id": "2088", "@value": "Dice (Primarily d20)"},
            {
                "@type": "rpgmechanic",
                "@id": "2124",
                "@value": "Lifepath Character Generation (Character starts at birth)",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2138",
                "@value": "Progression Tree (Skills, professions, magic abilities, etc.)",
            },
            {
                "@type": "rpgmechanic",
                "@id": "2094",
                "@value": "Skill Based (buy or gain skills)",
            },
            {
                "@type": "rpgpublisher",
                "@id": "22226",
                "@value": "Modiphius Entertainment",
            },
            {"@type": "rpgdesigner", "@id": "52214", "@value": "Jacob Ross"},
            {"@type": "rpgartist", "@id": "3", "@value": "(Uncredited)"},
            {"@type": "rpgproducer", "@id": "3", "@value": "(Uncredited)"},
        ],
        "description": "A Living Campaign Mission for 2269&#10;&#10;From the introduction:&#10;&#10;Remote mining colony Coriolanus IV failed to send its last scheduled status update, so Starfleet Command wants the Lexington to check in. It&rsquo;s the lone ship in the area, so the crew must operate without access to further support. Coriolanus IV is a mining colony that recently discovered one of the largest deposits of dilithium ever recorded, so it is critical to discover what happened and protect the deposits.&#10;&#10;",
        "yearpublished": {"@value": "2018"},
        "seriescode": {"@value": "STA TOS 3"},
    }