import os
from flask import Flask, render_template

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')
static_dir = os.path.join(base_dir, '..', 'static')

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

# ─────────────────────────────────────────────────────────
#  PLACES DATA
# ─────────────────────────────────────────────────────────
places = {
    "legazpi": {
        "name": "Legazpi City",
        "province": "Albay",
        "tagline": "Gateway to the Perfect Cone",
        "hero_color": "#c0392b",
        "description": "Legazpi City sits in the shadow of the iconic Mayon Volcano — the world's most perfectly shaped stratovolcano. A bustling port city and gateway to the rest of Bicol, it blends colonial charm with volcanic drama at every turn.",
        "image": "/static/images/Bicol/legazpicity.jpg",
        "image_hint": "mayon-volcano",
        "attractions": [
            {
                "name": "Mayon Volcano",
                "desc": "The world's most perfect volcanic cone, standing 2,463 meters tall. Hikers and thrill-seekers flock here for ATV rides across its lava fields and trekking adventures up its slopes.",
                "image": "/static/images/Bicol/legazpicity.mayonvolcano.jpg",
                "quick_facts": [
                    {"label": "Elevation", "value": "2,463 m (8,077 ft)"},
                    {"label": "Type", "value": "Active Stratovolcano"},
                    {"label": "Location", "value": "Albay, Bicol, Philippines"},
                    {"label": "Eruptions", "value": "52+ since 1616 CE"},
                    {"label": "Status", "value": "Most active in Philippines"},
                    {"label": "UNESCO", "value": "Albay Biosphere Reserve (2016)"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Rising 2,463 meters above the Albay Gulf, Mayon Volcano is the most iconic natural landmark in the Philippines — and arguably in all of Southeast Asia. Its near-perfect symmetrical cone, shaped by centuries of eruptions balanced by erosion, has inspired myths, art, and devotion for generations of Bicolanos."
                    },
                    {
                        "type": "heading",
                        "text": "The Perfect Cone"
                    },
                    {
                        "type": "text",
                        "text": "Mayon is a classic stratovolcano with a small central summit crater. Its near-perfect conical profile is no accident — geologists attribute it to a rare balance between the rate of eruption and the rate of erosion, defined by the angle of repose of its ash. The steepest upper slopes average a 75% gradient, while the lower foot slopes flatten to just 3%, creating the iconic hyperbolic sine curve seen from every corner of Albay."
                    },
                    {
                        "type": "fact-box",
                        "text": "Mayon is the centerpiece of the Albay Biosphere Reserve, declared by UNESCO in 2016. It is currently being nominated as a UNESCO World Heritage Site — a recognition of its extraordinary natural and cultural significance."
                    },
                    {
                        "type": "heading",
                        "text": "A History of Fire"
                    },
                    {
                        "type": "text",
                        "text": "Mayon is the most active volcano in the Philippines, with recorded eruptions stretching back to 1616 CE. In the past 500 years, it has erupted over 52 times. Its eruption styles range from Strombolian activity to basaltic Plinian columns, with cyclical behavior that typically begins with basaltic eruptions followed by longer periods of andesitic lava flows."
                    },
                    {
                        "type": "text",
                        "text": "Its most destructive eruption occurred on February 1, 1814, when a catastrophic event buried the town of Cagsawa under meters of tephra and lahar. An estimated 1,200 people perished — the single deadliest eruption in Mayon's recorded history. The ash from that event, combined with the equally catastrophic 1815 eruption of Indonesia's Mount Tambora, contributed to the global 'Year Without a Summer' in 1816."
                    },
                    {
                        "type": "quote",
                        "text": "At the date of my visit, the volcano had poured out, for five months continuously, a stream of lava on the Legaspi side from the very summit. The viscid mass bubbled quietly but grandly, and overran the border of the crater, descending several hundred feet in a glowing wave, like red-hot iron.",
                        "cite": "Samuel Kneeland, naturalist, Christmas Day, 1881"
                    },
                    {
                        "type": "heading",
                        "text": "Recent Activity (2024–2026)"
                    },
                    {
                        "type": "text",
                        "text": "Mayon remained active through 2024 and into 2026. A phreatic eruption on February 4, 2024 generated a 1,200-meter-high ash plume and pyroclastic flows, keeping the volcano at Alert Level 2. A briefer phreatic event on July 18, 2024 produced a 200-meter steam-and-ash plume that drifted west-northwest. In January 2026, activity escalated to Alert Level 3 as lava effusion resumed from the summit crater, with flows reaching up to 3.8 km down the Basud Gully on the eastern flank. PHIVOLCS continues to monitor the volcano closely; the permanent 6-kilometer Permanent Danger Zone (PDZ) around its summit remains strictly off-limits to the public at all times."
                    },
                    {
                        "type": "heading",
                        "text": "Visiting Mayon"
                    },
                    {
                        "type": "text",
                        "text": "Despite its activity, Mayon draws hundreds of thousands of visitors annually. The surrounding Mayon Volcano Natural Park — the first national park declared in the Philippines, on July 20, 1938 — offers multiple ways to experience the volcano up close. ATV rides across hardened lava fields bring adventurers within dramatic viewing distance of the cone, while organized treks up the lower slopes (subject to alert level conditions) reveal a landscape of alien beauty: black lava rivers, steam vents, and panoramic views over the Albay Gulf."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Visit at sunrise or early morning for the clearest views — clouds often shroud the summit by mid-morning.",
                            "Check PHIVOLCS bulletin daily (www.phivolcs.dost.gov.ph) before any planned activity near the volcano.",
                            "ATV tours can be arranged from Cagsawa Ruins Park — expect to pay ₱500–₱1,500 per person depending on route length.",
                            "The 6-km Permanent Danger Zone is strictly enforced; never attempt to enter it regardless of current alert level.",
                            "Lignon Hill Nature Park offers excellent elevated views of Mayon without the need to approach the volcano itself."
                        ]
                    }
                ]
            },
            {
                "name": "Cagsawa Ruins",
                "desc": "The haunting bell tower of an 18th-century church buried by the 1814 Mayon eruption. A striking reminder of nature's power, with Mayon looming perfectly in the background.",
                "image": "/static/images/Bicol/legazpicity.cagsawaruins.jpg",
                "quick_facts": [
                    {"label": "Location", "value": "Daraga, Albay"},
                    {"label": "Originally Built", "value": "1587 CE"},
                    {"label": "Destroyed", "value": "February 1, 1814"},
                    {"label": "Status", "value": "National Cultural Treasure"},
                    {"label": "Museum", "value": "Cagsawa National Museum (1992)"},
                    {"label": "Nearby Activity", "value": "ATV tours, zipline, SkyWheel"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "A solitary bell tower rising from a grassy park, framed perfectly by the cone of Mayon — the Cagsawa Ruins are among the most photographed and most haunting landmarks in the Philippines. They are what remains of a Franciscan church that once served a thriving colonial town, silenced in a single morning by one of history's most violent volcanic eruptions."
                    },
                    {
                        "type": "heading",
                        "text": "Birth, Destruction, Rebirth"
                    },
                    {
                        "type": "text",
                        "text": "The baroque church of Cagsawa was originally built in 1587 in the small town of Cagsaua during the Spanish colonial period. On July 25, 1636, Dutch pirates attacked and burned the church to the ground. It was patiently rebuilt in 1724 by Franciscan friars under Father Francisco Blanco, this time in stone, larger and stronger than before. Archaeological excavations by Bulacan State University have revealed that the Spanish architects incorporated Mesoamerican influences into the structure's design — a fascinating testament to the global reach of Spanish colonial culture."
                    },
                    {
                        "type": "text",
                        "text": "On February 1, 1814, Mayon Volcano unleashed its most violent recorded eruption. The town of Cagsawa and its surroundings were buried under several hundred million cubic meters of tephra and lahar, with ash accumulating to nine meters deep in places. Hundreds of townspeople sought refuge inside the stone church, trusting its sturdy walls to protect them. They were tragically mistaken — pyroclastic flows and lahar engulfed the building, and an estimated 1,200 to 2,000 people perished. Only the belfry and parts of the convent walls survived."
                    },
                    {
                        "type": "fact-box",
                        "text": "The facade of the Cagsawa church actually survived the 1814 eruption partially intact, as documented in photographs taken by American photographer Robert Larrimore Pendleton in the 1920s. Historical records show lava flows did not travel beyond the 6–7 km radius from the summit. The facade eventually collapsed due to earthquakes in the 1950s, leaving only the iconic belfry standing today."
                    },
                    {
                        "type": "heading",
                        "text": "A National Treasure"
                    },
                    {
                        "type": "text",
                        "text": "The Cagsawa Ruins have been declared a National Cultural Treasure of the Philippines. The site is now the centerpiece of Cagsawa Ruins Park, one of Albay's most-visited tourist destinations. Within the park stands the Cagsawa Branch of the National Museum of the Philippines (inaugurated October 30, 1992), which houses an extensive collection of photographs of Mayon's eruptions alongside geological and archaeological exhibits."
                    },
                    {
                        "type": "text",
                        "text": "When visitors walk the grounds of Cagsawa Ruins Park today, they are literally walking on top of the original town — the ruins they see represent only the upper portion of the church structure, with the lower half still entombed beneath the earth. A wooden cross marks what was once the church's altar, a solemn and deeply moving detail that transforms the site from a tourist attraction into a memorial."
                    },
                    {
                        "type": "heading",
                        "text": "Enduring Against All Odds"
                    },
                    {
                        "type": "text",
                        "text": "The resilience of the ruins is remarkable. In November 2006, Super Typhoon Reming (Durian) triggered catastrophic mudslides and lahar flows from Mayon that killed at least 1,266 people in the surrounding areas. The Cagsawa belfry stood unharmed. Survivors of the 1814 eruption had rebuilt their community in nearby Daraga, eventually merging the two settlements — a quiet act of resilience that echoes across two centuries."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Visit at sunrise (around 5:30–6:30 AM) for the best light on both the ruins and Mayon — golden hour photography here is extraordinary.",
                            "Aim for the early morning before clouds obscure Mayon's summit, typically by 9–10 AM.",
                            "The park also offers ATV tours, the Mayon SkyWheel Ferris ride, and zipline experiences.",
                            "Local vendors sell pili nuts, sili ice cream, and Mayon-themed souvenirs — the Pasalubong Center is worth a browse.",
                            "From here, you can also visit the intact Daraga Church (1773) and Lignon Hill Nature Park — a great half-day Albay circuit."
                        ]
                    }
                ]
            },
            {
                "name": "Sumlang Lake",
                "desc": "A serene crater lake offering bamboo raft rides with unobstructed views of Mayon Volcano. Best experienced at sunrise when the cone reflects off the still water.",
                "image": "/static/images/Bicol/legazpicity.sumlanglake.jpg",
                "quick_facts": [
                    {"label": "Type", "value": "Freshwater crater lake"},
                    {"label": "Location", "value": "Camalig, Albay"},
                    {"label": "Best Time", "value": "Sunrise (5:30–7 AM)"},
                    {"label": "Activity", "value": "Bamboo raft rides"},
                    {"label": "View of Mayon", "value": "Unobstructed from east side"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "On a still morning before the clouds arrive, Sumlang Lake offers one of the most breathtaking sights in all of the Philippines: the near-perfect reflection of Mayon Volcano shimmering on glassy water, framed by coconut palms and the soft glow of a Bicolano sunrise."
                    },
                    {
                        "type": "text",
                        "text": "Sumlang Lake is a small freshwater lake in the municipality of Camalig, Albay, situated to the east of Mayon Volcano. Its position makes it one of the few places where Mayon's full cone is visible without obstruction, and the lake's calm surface acts as a natural mirror for the volcano's reflection. Local boatmen pole visitors across the water on traditional bamboo rafts, a slow and meditative experience that stands in quiet contrast to the geological drama overhead."
                    },
                    {
                        "type": "fact-box",
                        "text": "Sumlang Lake is best visited between November and April, during the dry season, when Mayon's summit is more likely to be clear of clouds. The lake is also surrounded by productive rice paddies and coconut groves — the landscape itself is a portrait of daily Bicolano life."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Arrive before 6 AM for the best chance of a cloud-free Mayon — the summit is often wrapped in clouds by 8 AM.",
                            "Bamboo raft rides cost approximately ₱100–₱200 per person.",
                            "Bring insect repellent for early morning visits.",
                            "Sumlang Lake is easy to combine with a Cagsawa Ruins visit — both are within the same Camalig–Daraga circuit.",
                            "The surrounding rice fields are beautiful during planting season (June–July) and harvest (October–November)."
                        ]
                    }
                ]
            },
            {
                "name": "Legazpi Boulevard",
                "desc": "A scenic waterfront strip perfect for sunset strolls, street food, and panoramic views of the Albay Gulf with Mayon as the eternal backdrop.",
                "image": "/static/images/Bicol/legazpicity.legazpiboulevard.jpg",
                "quick_facts": [
                    {"label": "Location", "value": "Legazpi City, Albay"},
                    {"label": "Best Time", "value": "Sunset (5–6:30 PM)"},
                    {"label": "Facing", "value": "Albay Gulf, with Mayon behind"},
                    {"label": "Highlights", "value": "Street food, cycling, sunsets"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Legazpi Boulevard is the heartbeat of Legazpi City's social life — a palm-lined waterfront promenade where locals and visitors gather at dusk to watch the sun melt into the Albay Gulf while Mayon Volcano stands sentinel behind them."
                    },
                    {
                        "type": "text",
                        "text": "The boulevard stretches along the city's western waterfront, offering a wide pedestrian and cycling path flanked by benches, food stalls, and small parks. Street food vendors set up in the late afternoon, selling everything from grilled isaw and fishball skewers to fresh coconut juice and the local specialty: sili (chili) ice cream. On clear evenings, the boulevard provides an unobstructed view of Mayon's outline against the fading sky — one of the most quietly magnificent urban views in the Philippines."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Sunset visits (5–6:30 PM) offer the best light and atmosphere — locals call this their daily ritual.",
                            "Try the sili ice cream from boulevard vendors — a local specialty that balances sweet and heat.",
                            "Bicycle rentals are available along the boulevard for short periods.",
                            "On clear days, the boulevard also offers views across the gulf to the distant islands of the Lagonoy Gulf.",
                            "The nearby Embarcadero de Legazpi mall (a short walk inland) has good restaurants and a view deck if you want to end the evening indoors."
                        ]
                    }
                ]
            }
        ],
        "delicacies": [
            {
                "name": "Bicol Express",
                "desc": "The region's most famous dish — strips of pork slow-cooked in coconut milk with an avalanche of labuyo chilis and shrimp paste. Fiery, rich, and utterly addictive.",
                "image": "/static/images/Bicol/legazpicity.bicolexpress.jpg",
                "quick_facts": [
                    {"label": "Main Ingredients", "value": "Pork, coconut milk, labuyo chili, bagoong"},
                    {"label": "Origin", "value": "Bicol Region, Philippines"},
                    {"label": "Name Origin", "value": "Train route from Manila to Bicol"},
                    {"label": "Heat Level", "value": "Fiery (adjustable)"},
                    {"label": "Best Paired With", "value": "Steamed white rice"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Bicol Express is the dish that put the Bicol Region on the culinary map of the Philippines — a fierce, creamy, deeply satisfying stew of pork and labuyo chili simmered in coconut milk, with a funk of shrimp paste threading through every bite."
                    },
                    {
                        "type": "text",
                        "text": "Despite being named after the overnight passenger train that ran between Manila and Bicol (the 'Bicol Express'), the dish is actually believed to have originated in Malate, Manila, where Bicolano migrants brought their fiery cooking traditions. The version made in Bicol itself is often considered more austere and purer — the true expression of ginataang sili (chili cooked in coconut milk) that has been part of Bicolano food culture for centuries."
                    },
                    {
                        "type": "fact-box",
                        "text": "The labuyo chili used in Bicol Express is one of the spiciest varieties grown in the Philippines, measuring 80,000–100,000 Scoville Heat Units. For comparison, a jalapeño measures just 2,500–8,000 SHU. Bicolanos, raised on this heat since childhood, often find the dish mild — tourists are advised to start with caution."
                    },
                    {
                        "type": "text",
                        "text": "The base of the dish is coconut milk (gata), which tempers the ferocious heat of the chilies while adding a rich, slightly sweet creaminess. The pork — typically pork belly or shoulder — is cut into strips and slow-cooked until tender and fully infused with the flavors of the sauce. Bagoong (fermented shrimp paste) adds a savory, umami depth that elevates the entire dish beyond a simple chili stew."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "The best Bicol Express in Legazpi is found at local carinderias (small eateries) rather than tourist restaurants — look for bustling lunch spots near the public market.",
                            "Ask for it 'mild' if you're heat-sensitive; locals will understand and appreciate the honesty.",
                            "Eating it with heaping mounds of steamed white rice is not optional — it is required.",
                            "Leftovers taste even better the next day as the flavors deepen overnight.",
                            "Look for restaurants that make their own fresh gata (squeezed coconut milk) rather than using packaged coconut cream."
                        ]
                    }
                ]
            },
            {
                "name": "Pinangat",
                "desc": "Taro leaves stuffed with pork, shrimp, and gata (coconut milk), wrapped and slow-braised until tender. A Bicolano comfort food with deep earthy flavors.",
                "image": "/static/images/Bicol/legazpicity.pinangat.jpg",
                "quick_facts": [
                    {"label": "Main Ingredients", "value": "Taro leaves, pork, shrimp, coconut milk"},
                    {"label": "Also Known As", "value": "Laing (when dried)"},
                    {"label": "Cooking Method", "value": "Slow-braised in coconut milk"},
                    {"label": "Origin", "value": "Camarines Sur, Bicol"},
                    {"label": "Best Paired With", "value": "White rice, dried fish"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Pinangat is arguably Bicol's most beloved everyday dish — a humble packet of taro leaves wrapped around a filling of pork, shrimp, and spices, slowly braised in coconut milk until it becomes something extraordinary: earthy, creamy, tender, and deeply comforting."
                    },
                    {
                        "type": "text",
                        "text": "Though often confused with laing (its drier, more intensely flavored cousin), pinangat is distinguished by the use of fresh taro leaves and a more generously liquid coconut milk base. The leaves act as both wrapper and vegetable — they absorb the flavors of the filling and the gata during the long braise, becoming silky and rich while imparting their characteristic mild earthiness to the dish."
                    },
                    {
                        "type": "fact-box",
                        "text": "Taro leaves contain calcium oxalate crystals that cause an intense, unpleasant itching sensation if eaten raw. The prolonged cooking required for pinangat — often 45 minutes to an hour — is not just for flavor development: it is essential to break down these crystals and render the leaves safe and pleasant to eat."
                    },
                    {
                        "type": "text",
                        "text": "Every family in Bicol has their own pinangat recipe, passed down through generations. Some versions include small whole crabs alongside the pork and shrimp; others add siling labuyo for heat, or malunggay leaves for added nutrition. The dish is especially associated with the towns of Camarines Sur, where it is served at almost every family gathering, fiesta, and Sunday lunch."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "The best pinangat is found at home-style restaurants and carinderias — ask locals where their family's favorite is.",
                            "Don't mistake pinangat for laing; the former uses fresh leaves and has a creamier consistency, while laing uses dried leaves and is denser.",
                            "Pinangat is traditionally wrapped in fresh taro leaves and tied with strips of banana leaf or twine — the presentation itself is beautiful.",
                            "It pairs exceptionally well with dried fish (daing) and is best eaten the Filipino way: over a generous mound of warm rice."
                        ]
                    }
                ]
            },
            {
                "name": "Pili Candy",
                "desc": "Buttery, caramel-glazed pili nuts — a Bicol exclusive. The pili tree grows only in this region, making these sweet treats the ultimate pasalubong (homecoming gift).",
                "image": "/static/images/Bicol/legazpicity.pilicandy.jpg",
                "quick_facts": [
                    {"label": "Main Ingredient", "value": "Pili nut (Canarium ovatum)"},
                    {"label": "Endemic To", "value": "Bicol Region, Philippines"},
                    {"label": "Flavor", "value": "Rich, buttery, slightly sweet"},
                    {"label": "Varieties", "value": "Caramel, chocolate, salted, sugared"},
                    {"label": "Season", "value": "June–October (peak harvest)"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "If you leave Bicol with only one pasalubong (souvenir food), it should be pili candy. Made from the pili nut — a tree that grows only in the volcanic soils of the Bicol Region — these buttery, caramel-glazed treats are the edible emblem of the region, unavailable anywhere else on earth in their authentic form."
                    },
                    {
                        "type": "text",
                        "text": "The pili tree (Canarium ovatum) is an endemic Philippine species that thrives in the volcanic, well-drained soils of the Bicol Region. The nut itself is tear-drop shaped, encased in a hard shell within a fleshy outer husk. Once extracted and roasted, it reveals a rich, creamy, buttery kernel that tastes somewhat like a cross between a macadamia and an almond — but more distinctly its own thing. The fat content of the pili nut is extraordinarily high, making it one of the most calorie-dense nuts in the world."
                    },
                    {
                        "type": "fact-box",
                        "text": "The pili nut contains approximately 70% fat by weight — higher than macadamia nuts (75%) and almonds (49%). This remarkable fat content is what gives pili candy its distinctive melt-in-your-mouth quality and its extraordinary richness. Nutritionally, the fat is predominantly oleic acid (similar to olive oil), making pili nuts an unusually nutritious indulgence."
                    },
                    {
                        "type": "text",
                        "text": "Traditional pili candy is made by coating the roasted nuts in a hard caramel sugar glaze, sometimes with added butter for extra richness. Modern producers in Albay and Camarines Sur have expanded the range to include dark chocolate-coated pili, salted caramel pili, pili brittle, pili tarts, and even pili-based spreads and oils. The Albay province produces the largest quantity, and the towns of Oas and Sto. Domingo are particularly known for their pili confections."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Buy pili candy from established producers at the Pasalubong centers in Legazpi City for guaranteed quality.",
                            "Look for the Camalig-made varieties for particularly fresh nuts — the town is considered the pili capital of Albay.",
                            "Pili nuts can be purchased raw, roasted, or in confection form — raw nuts can be cooked at home and make excellent baking ingredients.",
                            "Store in a cool, dry place; the high fat content means pili nuts can go rancid faster than other nuts in warm weather.",
                            "The annual Pili Festival in Sto. Domingo, Albay, is dedicated to the nut and features cooking competitions and agricultural exhibits."
                        ]
                    }
                ]
            },
            {
                "name": "Kinunot",
                "desc": "Shredded stingray (pagi) or shark cooked in coconut cream with malunggay leaves and red hot peppers. A bold, unforgettable Bicolano classic.",
                "image": "/static/images/Bicol/legazpicity.kinunot.jpg",
                "quick_facts": [
                    {"label": "Main Protein", "value": "Stingray (pagi) or shark"},
                    {"label": "Base", "value": "Coconut cream (kakang gata)"},
                    {"label": "Key Flavors", "value": "Coconut, malunggay, labuyo chili"},
                    {"label": "Cooking Time", "value": "30–45 minutes"},
                    {"label": "Best Paired With", "value": "Steamed rice, dried fish"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Kinunot is one of the boldest expressions of Bicolano cuisine — shredded stingray or shark meat slow-cooked in rich coconut cream with the peppery brightness of malunggay (moringa) leaves and the fiery punch of red labuyo chili. It is a dish that surprises first-timers and becomes a lifelong craving."
                    },
                    {
                        "type": "text",
                        "text": "The name 'kinunot' comes from the Bicolano word meaning 'to shred,' describing the technique of manually pulling the cooked fish apart into fine, tender strands. Stingray (pagi) is the traditional choice, prized for its firm, slightly sweet flesh that holds up beautifully to the slow cooking and shreds cleanly. In some versions, small sharks (pating) are used instead, yielding a slightly different but equally satisfying texture."
                    },
                    {
                        "type": "text",
                        "text": "The malunggay (moringa) leaves added at the end of cooking bring a fresh, slightly bitter counterpoint to the rich coconut cream — a classic Bicolano technique of balancing richness with herbal freshness. The dish is finished with generous amounts of labuyo chili, whose heat cuts through the fat of the coconut milk and adds the region's signature fire."
                    },
                    {
                        "type": "fact-box",
                        "text": "Moringa (malunggay) leaves, a key ingredient in kinunot, are one of the most nutritionally dense greens in the world. They contain seven times the vitamin C of oranges, four times the calcium of milk, and four times the vitamin A of carrots. Their inclusion in kinunot is both a culinary and nutritional choice that reflects the Bicolano genius for combining pleasure and nourishment."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Kinunot is a staple of home cooking in Bicol — the best versions are found in family-run carinderias, not tourist restaurants.",
                            "Some restaurants in Legazpi offer 'kinunot na pagi' as a specialty — ask the staff if they make it in-house.",
                            "The dish is traditionally served in the palm-leaf wrappers or clay pots in which it was cooked — presentation varies.",
                            "If you're cooking it yourself, buy fresh pagi from the Legazpi public market, where the fish market section opens at dawn."
                        ]
                    }
                ]
            }
        ],
        "festivals": [
            {
                "name": "Ibalong Festival",
                "month": "August",
                "desc": "Legazpi's grandest celebration honoring the epic Ibalong, the ancient mythological saga of Bicol. Week-long street dancing, elaborate costumes depicting heroes and monsters, and cultural performances fill the city.",
                "image": "/static/images/Bicol/legazpicity.ibalongfestival.jpg",
                "quick_facts": [
                    {"label": "When", "value": "Last week of August"},
                    {"label": "Held In", "value": "Legazpi City, Albay"},
                    {"label": "Theme", "value": "Ibalong Epic (Bicolano mythology)"},
                    {"label": "Highlights", "value": "Street dancing, cultural shows, pageants"},
                    {"label": "Duration", "value": "5–7 days"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "The Ibalong Festival is Legazpi City's grandest annual celebration — a week-long tribute to the ancient mythological epic of Bicol, brought to life through elaborate street dancing, breathtaking costumes, and performances that transform the streets of Legazpi into the world of gods, heroes, and monsters."
                    },
                    {
                        "type": "text",
                        "text": "The festival is named after the 'Ibalong Epic' — Bicol's own ancient mythological cycle, comparable to Homer's Iliad or Virgil's Aeneid in its cultural significance. The epic tells of three demigod heroes — Baltog, Handyong, and Bantong — who battled terrifying monsters and supernatural forces to tame the wild land of Ibalong (the ancient name for the Bicol Region) and make it fit for human habitation."
                    },
                    {
                        "type": "text",
                        "text": "During the festival, contingents of street dancers from schools, barangays, and civic groups compete in elaborate themed performances, each interpreting scenes and characters from the Ibalong Epic. Costumes are extraordinarily detailed, featuring gigantic creature heads, body paint, feathered headdresses, and architectural props that recreate the mythological world in full color. The performances are judged on choreography, costume design, story presentation, and precision."
                    },
                    {
                        "type": "fact-box",
                        "text": "The Ibalong Epic was preserved and transcribed by Franciscan friar Fr. José Castaño in 1865, based on oral traditions he encountered in Bicol. The original text is a fragment of what scholars believe was a much longer oral epic, suggesting that the mythology of ancient Bicol was as rich and complex as any in Southeast Asia. It was declared a National Cultural Treasure by the National Commission for Culture and the Arts."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "The main street dancing competition is typically held on the last Saturday of August — this is the unmissable centerpiece of the festival.",
                            "Book accommodations in Legazpi at least two weeks in advance; hotels fill up quickly during Ibalong week.",
                            "The festival also features trade fairs, food festivals showcasing Bicolano cuisine, and a beauty pageant (Miss Ibalong).",
                            "Free viewing areas are available along the main parade route — arrive early for a good spot.",
                            "Photography is excellent during the festival; the elaborate costumes against the backdrop of Mayon make for extraordinary images."
                        ]
                    }
                ]
            },
            {
                "name": "Magayon Festival",
                "month": "May",
                "desc": "A month-long tourism festival celebrating Albay's natural and cultural beauty. Named after the legendary princess Magayon, it features trade fairs, beauty pageants, and pilgrimages around the volcano.",
                "image": "/static/images/Bicol/legazpicity.magayonfestival.jpg",
                "quick_facts": [
                    {"label": "When", "value": "Entire month of May"},
                    {"label": "Held In", "value": "Legazpi City & all of Albay"},
                    {"label": "Named After", "value": "Princess Daragang Magayon"},
                    {"label": "Duration", "value": "Full month"},
                    {"label": "Highlights", "value": "Pageants, trade fairs, volcano pilgrimages"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Every May, the entire province of Albay transforms into a month-long celebration called the Magayon Festival — a tourism showcase named after the legendary princess whose beauty and tragic love story, according to Bicolano mythology, gave birth to Mayon Volcano itself."
                    },
                    {
                        "type": "text",
                        "text": "The Magayon Festival was established to celebrate Albay's extraordinary natural and cultural heritage, centering on the province's most iconic asset: Mayon Volcano. Named after Daragang Magayon (Beautiful Maiden) — the legendary princess whose burial mound is said to have become Mayon — the festival is both a cultural celebration and a tourism promotion event that draws visitors from across the Philippines and internationally."
                    },
                    {
                        "type": "text",
                        "text": "The month-long program is packed with activities: the prestigious Miss Magayon beauty pageant, trade fairs and agricultural exhibitions, outdoor adventure events around the volcano (ATV rides, nature treks, cycling), food festivals showcasing Albay cuisine, cultural shows, and pilgrimages to significant sites around the province. The festival effectively serves as a month-long tourism week for the entire province."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "May is an excellent time to visit Albay — the pre-summer weather is warm but not yet at its most intense, and the festival adds a festive energy to everything.",
                            "Check the official Albay tourism calendar for the specific dates of major events within the Magayon Festival each year.",
                            "The Miss Magayon pageant is a prestigious event — tickets for the coronation night sell out quickly.",
                            "Trade fairs offer excellent opportunities to buy local products, crafts, and food items at competitive prices.",
                            "Adventure tourism events (ATV races, cycling tours) around Mayon are particularly popular during the festival."
                        ]
                    }
                ]
            }
        ],
        "myths": [
            {
                "name": "The Legend of Magayon",
                "desc": "Princess Daragang Magayon was so stunning that two chieftains waged war over her. In the battle, she and her beloved Panganoron were slain. From their burial mound grew Mayon Volcano, its perfect cone said to be Magayon's eternal beauty.",
                "image": "/static/images/Bicol/legazpicity.legendofmagayon.jpg",
                "quick_facts": [
                    {"label": "Type", "value": "Origin myth / love story"},
                    {"label": "Key Figures", "value": "Magayon, Panganoron, Pagtuga"},
                    {"label": "Subject", "value": "Origin of Mayon Volcano"},
                    {"label": "Theme", "value": "Beauty, jealousy, eternal love"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Long before Mayon Volcano had a name, before its perfect cone had been measured or explained by science, the people of Bicol knew its origin: a princess so beautiful that her death broke the earth, and from her grave grew a mountain as perfect as her face."
                    },
                    {
                        "type": "heading",
                        "text": "The Story of Daragang Magayon"
                    },
                    {
                        "type": "text",
                        "text": "In the ancient land of Ibalong, there lived a chieftain named Makusog who had a daughter of impossible beauty. Her name was Daragang Magayon — 'Beautiful Maiden' — and her loveliness was said to be so great that it caused the rivers to slow their current just to gaze at her reflection, and birds to land nearby to watch her pass."
                    },
                    {
                        "type": "text",
                        "text": "Two powerful chieftains sought her hand: Panganoron (Cloud), a kind and worthy young man who had won Magayon's heart, and Pagtuga (Eruption), a fierce and jealous rival who desired her as a prize. When Makusog accepted Panganoron's suit, Pagtuga was consumed by rage. He captured Magayon's father and threatened to kill him unless she agreed to marry him instead."
                    },
                    {
                        "type": "text",
                        "text": "Panganoron gathered his warriors and attacked Pagtuga's stronghold to rescue Magayon and her father. In the chaos of the battle, an arrow — loosed by one of Pagtuga's dying warriors — pierced Magayon through the heart. Panganoron reached her just as she fell, and the grief of her death shattered him. He died holding her, whispering her name."
                    },
                    {
                        "type": "quote",
                        "text": "They were buried together, and from the mound of their grave, a great mountain grew. Its cone rose perfect and symmetrical into the sky — shaped, the elders say, by the beauty of Magayon herself, who became the mountain so she could watch over Ibalong forever.",
                        "cite": "Bicolano oral tradition"
                    },
                    {
                        "type": "text",
                        "text": "The mountain was named Mayon — from 'Magayon,' 'the beautiful.' Its perfect cone is Magayon's perfect face, preserved in stone across centuries. When the volcano erupts with fire and ash, the old people of Bicol say it is Pagtuga — still raging, still jealous, still trying to possess what he could never have. And when clouds embrace the summit, they say it is Panganoron, wrapping his arms around his beloved for eternity."
                    },
                    {
                        "type": "fact-box",
                        "text": "The name 'Mayon' is indeed derived from 'Magayon,' the Bicolano word for 'beautiful.' The volcano's formal name in Central Bikol is 'Bulkan Mayon' — the Beautiful Volcano. The legend has been so central to Bicolano identity that the Magayon Festival is named in honor of the princess, and her image appears in official Albay provincial symbols."
                    }
                ]
            },
            {
                "name": "The Ibalong Epic",
                "desc": "Bicol's own mythological saga tells of three heroes — Baltog, Handyong, and Bantong — who battled monstrous creatures to tame the wild land of Ibalong (ancient Bicol).",
                "image": "/static/images/Bicol/legazpicity.ibalongepic.jpg",
                "quick_facts": [
                    {"label": "Type", "value": "Ancient oral epic / mythological cycle"},
                    {"label": "Key Heroes", "value": "Baltog, Handyong, Bantong"},
                    {"label": "Setting", "value": "Ancient Bicol (Ibalong)"},
                    {"label": "Transcribed", "value": "Fr. José Castaño, 1865"},
                    {"label": "Status", "value": "National Cultural Treasure"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Before there were highways, provinces, or cities — before even the name 'Bicol' — there was Ibalong, a wild and primordial land ruled by monsters, spirits, and the awesome forces of nature. The Ibalong Epic is Bicol's own ancient mythology: a cycle of hero tales that tells how the land was tamed, how civilization was born, and how three extraordinary men shaped the world that Bicolanos would come to inhabit."
                    },
                    {
                        "type": "heading",
                        "text": "The Three Heroes of Ibalong"
                    },
                    {
                        "type": "text",
                        "text": "The first hero was Baltog, who came from the divine lineage of Lipod (the Wind). He arrived in Ibalong and found the land terrorized by a monstrous wild boar called Tandayag, whose tusks were as long as a man and whose body was as large as a house. Baltog wrestled the beast barehanded and killed it, establishing the first human settlement on Ibalong's shores. He planted taro and built the first fields, becoming the founding father of Bicolano civilization."
                    },
                    {
                        "type": "text",
                        "text": "The second hero was Handyong — perhaps the greatest of the three — a warrior of supernatural ability who arrived to find Ibalong still plagued by terrors: Oryol, a half-human, half-serpent creature of cunning and beauty; a serpent with a thousand heads called Sarimaw; giant flying creatures and creatures of the deep. Handyong battled them all, sometimes with arms, sometimes with cunning. He eventually civilized Ibalong, instituting laws, crafts, governance, and the arts of writing."
                    },
                    {
                        "type": "quote",
                        "text": "Handyong taught the people to make boats and build houses, to weave cloth and fashion weapons, to write on leaves and to sing. He gave them law and gave them peace. And for a time, Ibalong was a paradise.",
                        "cite": "From the Ibalong Epic, transcribed by Fr. José Castaño (1865)"
                    },
                    {
                        "type": "text",
                        "text": "The third hero was Bantong, Handyong's greatest warrior. He was tasked with the seemingly impossible: to hunt and kill Rabot, a wild man of enormous power who could transform himself into stone. Bantong tracked Rabot for seven years, finally slaying him while the creature slept — using cunning where brute force had failed. With Rabot dead, the last of the great monsters of Ibalong was defeated, and the land was finally, fully, human."
                    },
                    {
                        "type": "fact-box",
                        "text": "The Ibalong Epic was preserved orally for centuries before Franciscan friar Fr. José Castaño transcribed it in Spanish in 1865. The text he recorded is believed to be only a fragment — scholars estimate the full epic may have been several times longer. The existing text was translated into English by Fenella Canilao and has been recognized as a National Cultural Treasure, placed alongside the Maranao 'Darangen' and Ifugao 'Hudhud' among the great oral literary traditions of the Philippines."
                    }
                ]
            }
        ]
    },
    "naga": {
        "name": "Naga City",
        "province": "Camarines Sur",
        "tagline": "Heart of Bicol",
        "hero_color": "#1a5276",
        "description": "Naga City is the cultural, commercial, and spiritual capital of the Bicol region. Home to the beloved Our Lady of Peñafrancia, it pulses with deep Catholic faith, colonial heritage, and a lively university town energy.",
        "image": "/static/images/Bicol/nagacity.header.jpg",
        "image_hint": "naga-city",
        "attractions": [
            {
                "name": "Basilica Minore of Our Lady of Peñafrancia",
                "desc": "The spiritual heart of Naga and all of Bicol. This grand basilica houses the miraculous image of the Ina (Mother) venerated by millions of devotees every year.",
                "image": "/static/images/Bicol/nagacity.bmolp.jpg",
                "quick_facts": [
                    {"label": "Full Name", "value": "Basilica Minore del Nuestra Señora de Peñafrancia"},
                    {"label": "Location", "value": "Naga City, Camarines Sur"},
                    {"label": "Status", "value": "Minor Basilica (Holy See)"},
                    {"label": "Patroness", "value": "Our Lady of Peñafrancia (Ina)"},
                    {"label": "Annual Pilgrims", "value": "~1.5 million (Peñafrancia Festival)"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "The Basilica Minore of Our Lady of Peñafrancia is the spiritual center not just of Naga, but of the entire Bicol Region. Every September, more than a million pilgrims converge on this church to honor 'Ina' — Mother — the beloved image of the Virgin Mary who has been the patroness of Bicolandia for over three centuries."
                    },
                    {
                        "type": "text",
                        "text": "The devotion to Our Lady of Peñafrancia traces its origins to 15th-century Spain, where a man named Simón Vela discovered a hidden image of the Virgin Mary in the rocky mountains of Peña de Francia in Salamanca. In the early 18th century, a Spanish seminarian named Miguel Robles de Covarrubias fell gravely ill in Manila. He prayed to Our Lady of Peñafrancia and experienced what he believed was a miraculous recovery. When he became a parish priest in Naga, he commissioned a stone image of the Virgin and enshrined her along the banks of the Naga River — fulfilling his vow. That shrine grew, over centuries, into the basilica that stands today."
                    },
                    {
                        "type": "text",
                        "text": "In 1924, the image received its Canonical Coronation — a papal recognition of its miraculous status — making the Our Lady of Peñafrancia one of the few crowned Marian images in the Philippines. In 2024, the Archdiocese of Cáceres celebrated the centennial of this coronation, drawing an estimated 1.5 million pilgrims and visitors to Naga, marking the largest single-year gathering in the festival's history. Pope Leo XIII had declared her the patroness of Naga City in 1895."
                    },
                    {
                        "type": "fact-box",
                        "text": "The Peñafrancia Festival is recognized as the largest Marian celebration in Asia, regularly drawing over 1.5 million participants. The 2024 Traslacion procession alone drew over 900,000 devotees to the streets of Naga City on a single afternoon, despite intermittent rain. Security personnel numbered 5,000, including 3,000 police officers."
                    },
                    {
                        "type": "heading",
                        "text": "The Peñafrancia Festival"
                    },
                    {
                        "type": "text",
                        "text": "Every September, the city transforms for the month-long Peñafrancia Festival. The highlight is the Traslacion — a massive procession in which Ina's image is carried from the basilica to the Naga Metropolitan Cathedral, the oldest church in Bicol, to begin a nine-day novena. A million voices rise in the streets: 'Viva la Virgen!' At the end of the novena, Ina returns by water in the spectacular Fluvial Procession — her flower-bedecked barge, the pagoda, gliding down the Naga River accompanied by thousands of boats and the fervent prayers and handkerchief-waving of the faithful lining the banks."
                    },
                    {
                        "type": "text",
                        "text": "The festival has not always been peaceful. On September 16, 1972, the Colgante Bridge collapsed under the weight of watching pilgrims, plunging hundreds into the Naga River. 138 people died from drowning, falling debris, and electrocution when power lines snapped into the water. The tragedy is remembered as one of the darkest moments in the festival's history, and safety infrastructure around the river has been dramatically improved since."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "The Basilica is open daily — visit outside of September for a quieter, more contemplative experience.",
                            "September visits should be planned well in advance: accommodations within Naga City book out weeks ahead of the festival.",
                            "The Traslacion (second Friday of September) and the Fluvial Procession (third Saturday) are the two unmissable events.",
                            "Dress modestly when entering the basilica — shoulders and knees should be covered.",
                            "The Peñafrancia Shrine and the Naga Metropolitan Cathedral (both nearby) are also worth visiting for a complete picture of the devotion."
                        ]
                    }
                ]
            },
            {
                "name": "Camarines Sur Watersports Complex",
                "desc": "One of Asia's premier cable wakeboarding parks. Whether you're a seasoned boarder or first-timer, the CamSur WakePark offers thrills on its Olympic-standard lake.",
                "image": "/static/images/Bicol/nagacity.camsurcomplex.jpg",
                "quick_facts": [
                    {"label": "Location", "value": "Pili, Camarines Sur"},
                    {"label": "Type", "value": "Cable wakeboarding park"},
                    {"label": "Cable System", "value": "Olympic-standard"},
                    {"label": "Activities", "value": "Wakeboarding, wakeskating, kneeboarding"},
                    {"label": "Best For", "value": "All levels, from beginners to pros"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "The Camarines Sur Watersports Complex (CWC) — better known as the CamSur WakePark — is Asia's premier cable wakeboarding destination, a world-class aquatic sports facility that brought international watersports competition to the heart of the Bicol Region."
                    },
                    {
                        "type": "text",
                        "text": "The WakePark operates a full-size Olympic-standard cable system on a large man-made lake, offering wakeboarding, wakeskating, and kneeboarding to riders of all skill levels. Beginners can take introductory lessons with trained instructors using beginner-friendly equipment, while advanced riders can attempt the course's ramps, rails, and kickers. The park has hosted multiple international wakeboarding competitions, drawing elite athletes from around the world to Camarines Sur."
                    },
                    {
                        "type": "fact-box",
                        "text": "Cable wakeboarding parks are considered more accessible and environmentally friendly than boat-pulled wakeboarding — the overhead cable system replaces the need for motorboats entirely, reducing fuel consumption, wake turbulence, and noise. The CamSur WakePark's Olympic-standard system can run multiple riders simultaneously on the same cable loop."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "No prior experience is needed — the park caters to absolute beginners and provides full instruction and equipment.",
                            "Book in advance during weekends and holidays, as the park can get busy.",
                            "The complex also has accommodation, restaurants, and a beach area on the lake — it's a full resort experience.",
                            "Wear a rash guard and water shoes for comfort; the park provides life jackets and helmets.",
                            "The park is located in Pili, Camarines Sur — approximately 30–45 minutes from Naga City by road."
                        ]
                    }
                ]
            },
            {
                "name": "Mt. Isarog National Park",
                "desc": "A cloud forest-draped inactive volcano offering pristine trails, waterfalls, and extraordinary biodiversity just outside Naga City.",
                "image": "/static/images/Bicol/nagacity.mtisarog.jpg",
                "quick_facts": [
                    {"label": "Elevation", "value": "1,966 m (6,450 ft)"},
                    {"label": "Type", "value": "Inactive stratovolcano / National Park"},
                    {"label": "Location", "value": "Camarines Sur, near Naga City"},
                    {"label": "Best For", "value": "Trekking, birdwatching, waterfalls"},
                    {"label": "Flora", "value": "Mossy cloud forest, endemic orchids"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "In the shadow of Bicol's more famous volcanic neighbor, Mt. Isarog stands as one of the region's great natural treasures — an inactive stratovolcano draped in extraordinary cloud forests, harboring endemic species found nowhere else on earth, and offering some of the finest mountain trekking in southern Luzon."
                    },
                    {
                        "type": "text",
                        "text": "Mt. Isarog National Park covers 10,112 hectares of protected forest in Camarines Sur, encompassing the mountain and its surrounding watershed. The mountain's slopes are covered in a mosaic of lowland forest, montane forest, and cloud forest at higher elevations, with remarkable biodiversity that includes numerous endemic plants, birds, and mammals. The Philippine cockatoo (kakak), the tarictic hornbill, and the Isarog shrew are among the notable fauna found here."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Register with the DENR office at the park entrance before attempting any trail — guides are required for summit treks.",
                            "The summit trek typically takes 2–3 days (camping overnight); day hikes to waterfalls and lower elevations are possible without overnight gear.",
                            "The best trekking season is November to May (dry season); trails can be treacherous during heavy rain.",
                            "The Malabsay Falls, a 15-meter cascade within the park, is accessible on a shorter day hike.",
                            "Bring layering clothes — temperatures at higher elevations can drop significantly even in summer."
                        ]
                    }
                ]
            },
            {
                "name": "Naga City Heritage District",
                "desc": "A compact zone of colonial-era buildings, the oldest church in Bicol, and the vibrant Naga City public market — the commercial and cultural soul of the Bicol capital.",
                "image": "/static/images/Bicol/nagacity.heritage.jpg",
                "quick_facts": [
                    {"label": "Location", "value": "Central Naga City, Camarines Sur"},
                    {"label": "Key Sites", "value": "Metropolitan Cathedral, Naga Museum, City Hall"},
                    {"label": "Best For", "value": "Walking tours, history, architecture"},
                    {"label": "Entry", "value": "Free (public spaces)"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Naga City's historic center is a compact, walkable district where colonial-era churches, Spanish-period buildings, and the lively pulse of a modern city coexist in fascinating layers. At its heart is the Naga Metropolitan Cathedral — the oldest church in the Bicol Region — and the rambling, sensory-overloading Naga City public market."
                    },
                    {
                        "type": "text",
                        "text": "The Naga Metropolitan Cathedral, formally the Parish of Saint John the Evangelist, is the oldest church in the Bicol Region, serving as the spiritual anchor of the city for centuries. It plays a central role in the Peñafrancia Festival each September, receiving the image of Our Lady of Peñafrancia during the Traslacion and housing her for the nine-day novena before her return by water to the basilica."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "A self-guided walking tour of the Heritage District takes approximately 2 hours — start at the Metropolitan Cathedral and work outward.",
                            "The Naga City Museum offers an excellent overview of the city's history and the Peñafrancia devotion.",
                            "The public market is at its most atmospheric in the early morning — the fish section, in particular, is a sensory feast.",
                            "Local guides are available for heritage walks; ask at the City Tourism Office."
                        ]
                    }
                ]
            }
        ],
        "delicacies": [
            {
                "name": "Laing",
                "desc": "Dried taro leaves slow-cooked in rich coconut cream with pork, shrimp, and chili until deeply concentrated and intensely flavorful. The definitive Bicolano comfort dish.",
                "image": "/static/images/Bicol/nagacity.laing.jpg",
                "quick_facts": [
                    {"label": "Main Ingredients", "value": "Dried taro leaves, coconut cream, pork/shrimp"},
                    {"label": "Vs Pinangat", "value": "Drier, more concentrated, uses dried leaves"},
                    {"label": "Cooking Time", "value": "1–1.5 hours minimum"},
                    {"label": "Heat Level", "value": "Moderate to hot (labuyo optional)"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Laing is to Bicol what adobo is to the rest of the Philippines — a dish so deeply embedded in the regional identity that its name alone evokes an entire way of life. Dried taro leaves, slow-cooked in coconut cream with pork and shrimp until the sauce has reduced to a concentrated, clingy, intensely flavorful coating: this is Bicolano comfort at its most essential."
                    },
                    {
                        "type": "text",
                        "text": "The critical distinction between laing and its close relative pinangat is the use of dried (rather than fresh) taro leaves, and the long, slow cooking process that reduces the coconut cream until it is almost entirely absorbed. The result is a dish that is drier, denser, and more powerfully flavored than pinangat — each leaf saturated with the combined essence of coconut, pork fat, shrimp, and chili."
                    },
                    {
                        "type": "fact-box",
                        "text": "A critical rule in making authentic laing: do not stir the taro leaves during the first half of cooking. Stirring prematurely breaks the leaves and releases their calcium oxalate crystals into the sauce, causing an unpleasant itching sensation in the throat. The leaves must be allowed to 'cook down' in the steam of the coconut cream before they are safe to combine with the rest of the dish."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Laing is ubiquitous in Naga and all of Bicol — every carinderia serves it, and quality is generally excellent.",
                            "It is best eaten the day it is made, while the coconut cream is still at peak freshness and creaminess.",
                            "Request 'spicy laing' if you want the full Bicolano experience with labuyo chili.",
                            "Laing makes an excellent pasalubong when vacuum-sealed — many producers in Naga City offer packaged versions for travel."
                        ]
                    }
                ]
            },
            {
                "name": "Pili Tart",
                "desc": "A buttery pastry shell filled with sweetened pili nut paste — Bicol's answer to the egg tart, richer and nuttier.",
                "image": "/static/images/Bicol/nagacity.pilitart.jpg",
                "quick_facts": [
                    {"label": "Main Ingredients", "value": "Pili nut, pastry shell, sugar, butter"},
                    {"label": "Texture", "value": "Crumbly pastry, dense nut filling"},
                    {"label": "Best Bought At", "value": "Naga City pasalubong shops"},
                    {"label": "Related To", "value": "Pili candy, pili brittle"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "The pili tart is one of the most beloved pastry traditions in all of Bicol — a buttery, crumbly shortcrust shell filled with a dense, sweetened pili nut paste that tastes like nothing else in the world. It is a small, perfect thing, and buying a box to bring home is a near-sacred obligation for any visitor to Naga City."
                    },
                    {
                        "type": "text",
                        "text": "The filling is made from roasted pili kernels ground into a paste and sweetened with sugar and butter, creating something with the density of marzipan but a distinctly different, earthier, nuttier flavor. The pastry shell is typically shortcrust — flaky, buttery, and designed to complement rather than overshadow the nut filling. Some bakers add a thin layer of egg custard over the pili paste, creating a hybrid that bridges the Chinese-influenced egg tart tradition with Bicolano ingredients."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Buy pili tarts from established pasalubong shops in Naga City for the best quality — look for shops that bake fresh daily.",
                            "Pili tarts are best eaten at room temperature on the day of purchase.",
                            "They make excellent gifts — individual boxes of 6 or 12 tarts are typically available.",
                            "Look for artisanal bakeries that use freshly ground pili paste rather than pre-made filling."
                        ]
                    }
                ]
            },
            {
                "name": "Pancit Bato",
                "desc": "Thick, slightly rough-textured rice noodles from the town of Bato, Camarines Sur — a Bicolano pasta unique to the region.",
                "image": "/static/images/Bicol/nagacity.pancitbato.jpg",
                "quick_facts": [
                    {"label": "Noodle Type", "value": "Thick, sun-dried rice noodles"},
                    {"label": "Origin", "value": "Bato, Camarines Sur"},
                    {"label": "Key Feature", "value": "Rough texture, chewier than standard noodles"},
                    {"label": "Common Serving", "value": "Stir-fried with pork, vegetables, soy sauce"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Pancit Bato is Bicol's own noodle tradition — thick, slightly rough-textured rice noodles from the town of Bato in Camarines Sur, with a chewiness and substance that sets them apart from the fine vermicelli used in most Filipino pancit dishes."
                    },
                    {
                        "type": "text",
                        "text": "Unlike the thin rice noodles (bihon) or egg noodles (canton) that dominate mainstream Filipino pancit, Pancit Bato uses thick, sun-dried rice noodles with a rustic, hand-made quality. The rough surface of the noodles clings to sauces and absorbs flavors more readily than smoother commercial varieties, giving the dish a heartier, more satisfying quality. They are typically stir-fried with pork, vegetables, and soy-based sauces, often with calamansi (Philippine lime) on the side."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Pancit Bato noodles are available dried in pasalubong shops throughout Naga City and Camarines Sur — they travel well.",
                            "The best prepared Pancit Bato is found in traditional restaurants in Naga City and in Bato town itself.",
                            "Soak dried Pancit Bato noodles in warm water for 15–20 minutes before cooking to achieve the right texture."
                        ]
                    }
                ]
            },
            {
                "name": "Tinutungan",
                "desc": "Chicken or pork cooked in burnt coconut (tunu) cream — a uniquely Bicolano technique that gives the dish a smoky, complex coconut flavor.",
                "image": "/static/images/Bicol/nagacity.tinutungan.jpg",
                "quick_facts": [
                    {"label": "Key Technique", "value": "Burnt (tunu) coconut cream"},
                    {"label": "Main Protein", "value": "Chicken or pork"},
                    {"label": "Flavor Profile", "value": "Smoky, nutty, rich coconut"},
                    {"label": "Origin", "value": "Bicol Region, Philippines"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Tinutungan is one of Bicol's most distinctive and underappreciated culinary achievements — a dish built on a technique unique to the region: the deliberate charring of fresh coconut flesh before extracting the cream, which imparts a deep, smoky, nutty character to everything it touches."
                    },
                    {
                        "type": "text",
                        "text": "The word 'tinutungan' comes from 'tunu,' meaning 'to burn' or 'to char.' Fresh coconut flesh is roasted or toasted until darkened before being grated and pressed for cream, and the resulting gata has a dramatically different flavor from standard coconut milk — complex, smoky, with a nuttiness that recalls toasted sesame or roasted macadamia. This burnt coconut cream is then used to cook chicken or pork in a slow braise, absorbing the flavors of aromatics like garlic, onion, and ginger while the smokiness intensifies."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Tinutungan is a specialty dish not always found in everyday carinderias — seek out restaurants that specialize in traditional Bicolano cooking.",
                            "The smoky flavor is subtle in well-made versions; if it tastes acrid or bitter, the coconut was over-charred.",
                            "It pairs beautifully with plain steamed rice and a simple vegetable side dish.",
                            "Ask Naga City locals for their recommended 'lutong Bicol' (Bicolano cooking) restaurants — this is where you'll find tinutungan."
                        ]
                    }
                ]
            }
        ],
        "festivals": [
            {
                "name": "Peñafrancia Festival",
                "month": "September",
                "desc": "Asia's largest Marian celebration, drawing 1.5 million devotees to Naga every September. The highlight is the spectacular Fluvial Procession on the Naga River, where the image of Ina returns to her basilica by barge.",
                "image": "/static/images/Bicol/nagacity.penafrancia.jpg",
                "quick_facts": [
                    {"label": "When", "value": "Third Sunday of September (month-long)"},
                    {"label": "Annual Pilgrims", "value": "~1.5 million"},
                    {"label": "Key Events", "value": "Traslacion, Novena, Fluvial Procession"},
                    {"label": "Recognition", "value": "Largest Marian festival in Asia"},
                    {"label": "Since", "value": "Early 18th century"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Every September, Naga City becomes the center of the Catholic world in Asia. More than a million and a half pilgrims — from across the Philippines, from the Filipino diaspora, from across the globe — converge on this mid-sized Bicolano city to honor 'Ina,' the beloved Virgin of Peñafrancia, patroness of Bicol. What unfolds is the largest Marian celebration in Asia: the Peñafrancia Festival."
                    },
                    {
                        "type": "heading",
                        "text": "Three Centuries of Faith"
                    },
                    {
                        "type": "text",
                        "text": "The devotion to Our Lady of Peñafrancia in Naga was established in the early 18th century — around 1712 — when Spanish priest Fr. Miguel Robles de Covarrubias enshrined his replica of the Virgin along the Naga River after she reportedly interceded in his recovery from a grave illness. Miracles continued to be attributed to the image, and the devotion grew rapidly. In 1864, Bishop Francisco Gainza formalized the Traslacion procession, creating the tradition that continues today for over 160 years."
                    },
                    {
                        "type": "text",
                        "text": "The Traslacion marks the festival's religious high point: on the second Friday of September, Ina's image is carried from the Basilica Minore through the streets of Naga to the Metropolitan Cathedral, with hundreds of thousands of devotees following on foot, chanting 'Viva la Virgen!' The procession takes hours as the crowd surges through streets normally reserved for traffic, the air thick with incense and prayer. Nine days of novena follow, with masses packed beyond capacity every morning and evening."
                    },
                    {
                        "type": "text",
                        "text": "The climax arrives on the Fluvial Procession — the third Saturday of September — when Ina's image, aboard a grand flower-bedecked barge called the pagoda, sails back down the Naga River to the basilica. Thousands of boats escort her; thousands more line the riverbanks waving white handkerchiefs, shouting prayers and chants, tears streaming down faces that have made this pilgrimage for fifty years. As the pagoda reaches the basilica, fireworks erupt over the river. It is one of the most moving religious spectacles in Southeast Asia."
                    },
                    {
                        "type": "fact-box",
                        "text": "The 2024 Peñafrancia Festival marked the centennial of the image's Canonical Coronation by the Holy See in 1924. Over 900,000 devotees lined the streets for the Traslacion alone on September 13, 2024, making it one of the most-attended single-day religious events in Philippine history. Total festival attendance reached an estimated 1.5 million across the entire celebration period."
                    },
                    {
                        "type": "heading",
                        "text": "Beyond the Processions"
                    },
                    {
                        "type": "text",
                        "text": "The Peñafrancia Festival is not only a religious event — it is a month-long cultural celebration. The Miss Bicolandia beauty pageant, considered the oldest pageant in Bicol, is held during the festival period. The Voyadores Street Dancing competition transforms Naga's streets into a color-saturated celebration of Bicolano culture. Trade fairs, food festivals, musical performances, and the Marian Youth Congress run throughout the month, making September Naga City's most vibrant and hospitable time to visit."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "Book accommodations in Naga City at least 3–4 weeks in advance for September visits — everything fills up.",
                            "The Traslacion (second Friday of September) and the Fluvial Procession (third Saturday) are the two unmissable events.",
                            "Position yourself along the Naga River early on the day of the Fluvial Procession — riverbank spots fill hours before the pagoda passes.",
                            "September weather in Naga can bring afternoon rain — bring an umbrella that won't block the view of others.",
                            "Drone use during processions is strictly prohibited by joint order of the Archdiocese, city government, and PNP.",
                            "The festival's cultural events (Voyadores, parades, trade fair) are excellent for photography and are generally less crowded than the religious processions."
                        ]
                    }
                ]
            },
            {
                "name": "Naga City Fiesta",
                "month": "June",
                "desc": "The feast day of Saint John the Evangelist, patron of Naga City — a week of religious celebrations, cultural events, and community gatherings marking the city's founding.",
                "image": "/static/images/Bicol/nagacity.2ndfest.jpg",
                "quick_facts": [
                    {"label": "Patron", "value": "Saint John the Evangelist"},
                    {"label": "Feast Day", "value": "June (around June 24)"},
                    {"label": "Duration", "value": "Several days"},
                    {"label": "Highlights", "value": "Solemn Mass, procession, cultural events"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Naga City's annual fiesta in honor of Saint John the Evangelist — the city's patron saint — is a quieter but deeply meaningful celebration that brings the community together in faith, food, and civic pride every June."
                    },
                    {
                        "type": "text",
                        "text": "The Naga City Fiesta celebrates the feast of Saint John the Evangelist, whose parish church — the Naga Metropolitan Cathedral — is the oldest church in the Bicol Region. The celebration features solemn masses, processions, cultural performances, and the traditional community gatherings that define Philippine fiesta culture: open houses, shared meals, reunions of families and friends, and the particular warmth that comes when an entire city celebrates together."
                    },
                    {
                        "type": "tips",
                        "items": [
                            "The Naga City fiesta is an excellent time to experience authentic Filipino fiesta culture without the overwhelming crowds of September.",
                            "Local restaurants and carinderias offer special fiesta menus — look for traditional Naga City dishes prepared only during celebrations.",
                            "The solemn procession around the cathedral is a beautiful and photogenic event, especially in the early evening.",
                            "Ask locals if any barangay fiestas are running concurrently — barangay-level celebrations often offer more intimate, authentic experiences."
                        ]
                    }
                ]
            }
        ],
        "myths": [
            {
                "name": "The Miracle of Peñafrancia",
                "desc": "In the early 1700s, a young Spanish priest fell gravely ill. He promised to bring a replica of Our Lady of Peñafrancia to Naga if cured. Upon his miraculous recovery, he kept his vow — and a three-century devotion was born.",
                "image": "/static/images/Bicol/nagacity.1stmyth.jpg",
                "quick_facts": [
                    {"label": "Type", "value": "Religious origin story / miracle"},
                    {"label": "Key Figure", "value": "Fr. Miguel Robles de Covarrubias"},
                    {"label": "Year", "value": "~1712"},
                    {"label": "Significance", "value": "Origin of Peñafrancia Festival"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Great devotions often begin with a single act of desperate faith — a prayer uttered in extremis, a vow made in the darkness of illness. The story of Our Lady of Peñafrancia's coming to Bicol is one such story: a young man, sick and far from home, who made a promise to the Virgin and lived to keep it, changing Bicolano history forever."
                    },
                    {
                        "type": "text",
                        "text": "In the early 18th century, a Spanish seminarian named Miguel Robles de Covarrubias was studying at the University of Santo Tomas in Manila when he fell gravely ill. Fearing death, he prayed fervently to Our Lady of Peñafrancia — a Marian image venerated in Salamanca, Spain, from where his family came. He promised the Virgin that if he recovered, he would bring her image to whatever parish he would serve in the Philippines."
                    },
                    {
                        "type": "text",
                        "text": "He recovered. When he was ordained and assigned as parish priest to Naga City in Camarines Sur, he kept his vow. Around 1712, he commissioned a stone image of Our Lady of Peñafrancia and enshrined it in a small chapel along the banks of the Naga River. Almost immediately, miracles were attributed to her intercession: healings, rescues, inexplicable recoveries from illness. Word spread through the Bicol Region and beyond. The chapel grew into a church, the church into the basilica that stands today."
                    },
                    {
                        "type": "quote",
                        "text": "She became not just a patron but a mother — 'Ina' — to everyone in Bicol who had ever been sick, lost, or afraid. Three centuries later, a million people still come to her river every September to say thank you.",
                        "cite": "From the Archdiocese of Cáceres historical records"
                    },
                    {
                        "type": "fact-box",
                        "text": "The devotion to Our Lady of Peñafrancia is now celebrated not only in Naga City but wherever Bicolanos have settled — including the United States, where the Feast of Our Lady of Peñafrancia is one of the oldest and largest Filipino Marian celebrations in San Diego, California, with nearly 50 years of continuous celebration."
                    }
                ]
            },
            {
                "name": "The Origin of the Bicol River",
                "desc": "Local legend tells that the Bicol River was carved by a giant serpent — the Naga — that slithered from the mountains to the sea, its body cutting through the earth to create the great waterway.",
                "image": "/static/images/Bicol/nagacity.2ndmyth.jpg",
                "quick_facts": [
                    {"label": "Type", "value": "Geographic origin legend"},
                    {"label": "Key Figure", "value": "The Naga (great serpent)"},
                    {"label": "Subject", "value": "Origin of Naga City's name & the Bicol River"},
                    {"label": "Significance", "value": "Explains city name 'Naga'"},
                ],
                "content": [
                    {
                        "type": "lead",
                        "text": "Why is a city named Naga? Why does the Bicol River wind through the lowlands with its distinctive, serpentine curves? The old people of Camarines Sur have always known the answer: there was a great serpent — the Naga — and everything follows from that."
                    },
                    {
                        "type": "text",
                        "text": "In Bicolano legend, the Naga was not a malevolent creature but a vast, ancient serpent of supernatural power — an embodiment of the earth's energy, related to the nāga of Hindu and Buddhist cosmology that the ancient peoples of Southeast Asia revered. The Naga lived in the mountains of what is now Camarines Sur, coiling among the peaks and drawing its power from the earth."
                    },
                    {
                        "type": "text",
                        "text": "One day — at the beginning of time, when the land was still being shaped — the Naga began to move. It slithered down from the mountains toward the sea, its enormous body carving a path through the soft earth of the lowlands. The weight and movement of the serpent cut deeper and deeper channels as it moved, and when it finally reached the sea and disappeared into the water, the groove it had made in the earth began to fill with rain and spring water. That channel became the Bicol River — the great waterway that sustains the heart of the region to this day."
                    },
                    {
                        "type": "text",
                        "text": "The city that grew near the river's headwaters, in the place where the Naga was said to have begun its great journey, was named for the serpent: Naga. The river's characteristic winding curves — visible even on modern maps — are explained by the sinuous movement of the serpent's body as it cut its path. In this way, the serpent that departed gave the land its shape and gave the city its name."
                    },
                    {
                        "type": "fact-box",
                        "text": "The Bicol River is the longest river in the Bicol Region, stretching approximately 64 kilometers through the Camarines Sur lowlands before emptying into the San Miguel Bay. It is the primary water source and traditional transportation corridor for dozens of municipalities, and the backdrop to the Peñafrancia Fluvial Procession each September — a river mythologically born of a serpent, now hosting a river procession of faith."
                    }
                ]
            }
        ]
    },
    "sorsogon": {
        "name": "Sorsogon City",
        "province": "Sorsogon",
        "tagline": "Where Land Meets the Whale Shark",
        "hero_color": "#1e8449",
        "description": "At the southernmost tip of Luzon, Sorsogon is where the Bicol Peninsula meets the sea. Famous for whale shark encounters, natural hot springs, and pristine beaches, it is Bicol's wild, unhurried edge.",
        "image": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=1200&q=80",
        "image_hint": "sorsogon-whale-shark",
        "attractions": [
            {
                "name": "Donsol Whale Shark Interaction",
                "desc": "Swimming alongside butanding (whale sharks) in their natural habitat. Donsol is considered one of the world's best places for ethical whale shark encounters.",
                "quick_facts": [
                    {"label": "Season", "value": "November to June"},
                    {"label": "Location", "value": "Donsol, Sorsogon"},
                    {"label": "Type", "value": "Ethical snorkeling (no feeding/touching)"},
                ],
                "content": [
                    {"type": "lead", "text": "Donsol in Sorsogon is where the world's largest fish — the whale shark — congregates in extraordinary numbers from November to June. Ethical, cage-free encounters allow snorkelers to swim alongside these gentle giants in their natural environment."},
                    {"type": "text", "text": "The whale sharks of Donsol aggregate in the nutrient-rich waters off the Sorsogon coast to feed on plankton blooms. Unlike shark-feeding attractions elsewhere, Donsol's butanding interaction program prohibits feeding, touching, or riding the animals, and strictly regulates boat numbers. Interaction Officers (BIOs) on each boat ensure rules are followed, making it one of the most responsible whale shark tourism programs in the world."},
                    {"type": "tips", "items": ["Book through the WWF-accredited Donsol Butanding Interaction Center in advance during peak season.", "The best months are January to May for the highest butanding sightings.", "Bring a wide-angle camera or GoPro and strong fins — the sharks move faster than you expect."]}
                ]
            },
            {
                "name": "Bulusan Volcano Natural Park",
                "desc": "A UNESCO-recognized natural park surrounding the active Bulusan Volcano with crater lake, rainforest trails, and lake swimming holes.",
                "quick_facts": [
                    {"label": "Elevation", "value": "1,565 m"},
                    {"label": "Status", "value": "Active volcano"},
                    {"label": "UNESCO", "value": "Natural Park designation"},
                ],
                "content": [
                    {"type": "lead", "text": "Bulusan Volcano, the southernmost active volcano in Luzon, rises above a natural park of extraordinary beauty in Sorsogon province — crater lakes, hot springs, rainforest trails, and biodiversity that rivals any protected area in the Philippines."},
                    {"type": "text", "text": "Bulusan Volcano Natural Park encompasses 3,673 hectares of protected forest and volcanic landscape surrounding the active Bulusan Volcano. The park's most visited feature is Lake Bulusan — a tranquil, emerald-green volcanic crater lake perfect for swimming and kayaking, set against the forested slopes of the volcano."},
                    {"type": "tips", "items": ["Register with the DENR office before entering the park.", "Lake Bulusan is the most accessible destination — a short hike from the park entrance.", "Check PHIVOLCS bulletins before visiting as Bulusan remains an active volcano."]}
                ]
            },
            {
                "name": "Barcelona Church and Watchtower",
                "desc": "A beautifully preserved 17th-century Spanish colonial church and watchtower, built to watch for pirate raids along the Sorsogon coast.",
                "quick_facts": [
                    {"label": "Built", "value": "17th century"},
                    {"label": "Location", "value": "Barcelona, Sorsogon"},
                    {"label": "Status", "value": "National Cultural Treasure"},
                ],
                "content": [
                    {"type": "lead", "text": "The church and watchtower of Barcelona in Sorsogon are among the finest surviving examples of Spanish colonial fortified ecclesiastical architecture in the Philippines — a stunning testament to the era when coastal communities lived under constant threat of Moro pirate raids."},
                    {"type": "text", "text": "The Barcelona Church (formally the Saint Anne Parish Church) was built in the 17th century by Spanish friars and local laborers, alongside a coral stone watchtower from which sentinels could scan the waters for approaching pirates. The complex has survived centuries of typhoons, earthquakes, and neglect to stand today as a National Cultural Treasure."},
                    {"type": "tips", "items": ["The watchtower interior is accessible with a small fee — climb it for coastal views.", "Barcelona town is approximately 30 minutes from Sorsogon City by road.", "Combine the visit with a stop at nearby Bitaog Beach for a complete Barcelona day trip."]}
                ]
            },
            {
                "name": "Rizal Beach",
                "desc": "A long stretch of gray-black volcanic sand in Gubat, Sorsogon, known for consistent surf and dramatic atmosphere.",
                "quick_facts": [
                    {"label": "Location", "value": "Gubat, Sorsogon"},
                    {"label": "Sand Color", "value": "Gray-black volcanic"},
                    {"label": "Surfing", "value": "Consistent reef and beach breaks"},
                ],
                "content": [
                    {"type": "lead", "text": "Rizal Beach in Gubat, Sorsogon, is Bicol's surfing secret — a long, dramatic stretch of dark volcanic sand facing the Pacific, with consistent surf breaks and the kind of unhurried, local atmosphere that more famous surf destinations lost decades ago."},
                    {"type": "text", "text": "The beach's distinctive gray-black sand comes from the volcanic geology of Sorsogon, giving it a dramatic, almost otherworldly appearance compared to the white-sand beaches of more famous Philippine destinations. Surfers prize the consistent waves generated by Pacific swells, particularly from October to March. The town of Gubat remains pleasantly uncommercial — a few surf shacks, local restaurants serving fresh seafood, and a beach road lined with coconut palms."},
                    {"type": "tips", "items": ["Surfboard rental is available from local surf schools in Gubat town.", "Non-surfers can enjoy the beach for swimming in calmer conditions — ask locals about the safest swimming areas.", "The beach is most atmospheric at sunset, when the dark sand turns gold and the Pacific horizon glows."]}
                ]
            }
        ],
        "delicacies": [
            {"name": "Butanding Fingers", "desc": "Deep-fried banana fritters named in playful tribute to Donsol's whale sharks.", "image": None,
             "quick_facts": [{"label": "Type", "value": "Street food / snack"}, {"label": "Main Ingredient", "value": "Banana (saba)"}],
             "content": [{"type": "lead", "text": "Not actual whale shark — just a delightful local joke. Butanding Fingers are deep-fried banana fritters shaped like fingers, named in cheerful tribute to the gentle giants of Donsol Bay."}, {"type": "tips", "items": ["Find them at street food stalls near Donsol pier and in Sorsogon City markets."]}]},
            {"name": "Hardinera", "desc": "A festive Sorsogon meatloaf baked with pork, chorizo, eggs, and pineapple.", "image": None,
             "quick_facts": [{"label": "Type", "value": "Festive meatloaf"}, {"label": "Origin", "value": "Sorsogon, Bicol"}],
             "content": [{"type": "lead", "text": "Hardinera is Sorsogon's festive meatloaf — a colorful, hearty baked dish of pork, chorizo, hard-boiled eggs, bell peppers, and pineapple pressed into a llanera mold, unmolded to reveal a mosaic of flavors and colors."}, {"type": "tips", "items": ["Hardinera is a holiday and celebration dish — find it at Sorsogon City restaurants during fiestas and special events."]}]},
            {"name": "Pili Tart", "desc": "Buttery pastry shell filled with sweetened pili nut paste.", "image": None,
             "quick_facts": [{"label": "Type", "value": "Pastry / pasalubong"}],
             "content": [{"type": "lead", "text": "Sorsogon's bakeries produce excellent pili tarts — small, buttery pastry cups filled with sweetened pili nut paste that melt in the mouth."}, {"type": "tips", "items": ["Buy fresh from local bakeries in Sorsogon City, particularly near the public market area."]}]},
            {"name": "Ginataang Puso ng Saging", "desc": "Banana blossom braised in coconut milk with pork and chili.", "image": None,
             "quick_facts": [{"label": "Main Ingredient", "value": "Banana blossom (heart)"}, {"label": "Base", "value": "Coconut milk"}],
             "content": [{"type": "lead", "text": "Banana blossom (puso ng saging) braised in coconut milk with pork and labuyo chili — a humble, deeply satisfying dish that showcases Bicolano genius for transforming simple ingredients."}, {"type": "tips", "items": ["A staple of home cooking in Sorsogon — ask at family-run carinderias for the freshest versions."]}]}
        ],
        "festivals": [
            {"name": "Kasanggayahan Festival", "month": "October", "desc": "Sorsogon's founding anniversary celebration featuring street dancing, cultural presentations, agri-trade fairs, and beauty pageants.", "image": None,
             "quick_facts": [{"label": "When", "value": "October (founding anniversary)"}, {"label": "Duration", "value": "Several days"}],
             "content": [{"type": "lead", "text": "The Kasanggayahan Festival marks Sorsogon province's founding anniversary with a week-long celebration of the province's diverse heritage, natural wonders, and community spirit."}, {"type": "tips", "items": ["October is an excellent time to visit Sorsogon City — the festival adds festivity to the start of the whale shark season."]}]},
            {"name": "Butanding Festival", "month": "November", "desc": "Held in Donsol to welcome the annual return of the whale sharks, with coastal clean-ups, marine conservation forums, and cultural nights.", "image": None,
             "quick_facts": [{"label": "When", "value": "November"}, {"label": "Location", "value": "Donsol, Sorsogon"}],
             "content": [{"type": "lead", "text": "The Butanding Festival in Donsol celebrates the annual return of whale sharks to Sorsogon waters — combining environmental advocacy, cultural celebration, and the official opening of the butanding interaction season."}, {"type": "tips", "items": ["Attending the Butanding Festival means the interaction season has just opened — secure your BIO appointment immediately."]}]}
        ],
        "myths": [
            {"name": "The Origin of the Butanding", "desc": "In Donsol folklore, the whale sharks were once ferrymen for the gods who chose to remain in the warm waters as guardians of the passage.", "image": None,
             "quick_facts": [{"label": "Type", "value": "Origin myth"}, {"label": "Subject", "value": "Whale shark / butanding"}],
             "content": [{"type": "lead", "text": "The whale sharks of Donsol are not just fish to the people who have lived beside them for generations — they are sacred presences, ancient beings with a purpose and a story."}, {"type": "text", "text": "In Donsol folklore, the whale sharks were once gentle giants who served as ferrymen for the gods, carrying souls across the great waters between worlds. When the gods departed, the butanding chose to remain in Donsol's warm waters — guardians of the passage, too kind to leave the mortals they had grown to love."}]},
            {"name": "The Sleeping Bulusan", "desc": "Bulusan Volcano is not a mountain but a sleeping giant who fell into eternal slumber after a great battle with the sea.", "image": None,
             "quick_facts": [{"label": "Type", "value": "Origin myth"}, {"label": "Subject", "value": "Bulusan Volcano"}],
             "content": [{"type": "lead", "text": "The people of southern Sorsogon have always known that Bulusan Volcano is not simply a mountain — it is a sleeping giant, and when the earth trembles or steam rises from the crater, he stirs in an ancient dream."}, {"type": "text", "text": "Local legend holds that Bulusan Volcano is not a mountain at all but a sleeping giant who fell into eternal slumber after a great battle with the sea. When the earth shakes or steam rises from the crater, the elders say he stirs in his sleep, dreaming of the ocean he once fought — and the lover he lost to its depths."}]}
        ]
    }
}

# ─────────────────────────────────────────────────────────
#  CATEGORY METADATA
# ─────────────────────────────────────────────────────────
SECTION_META = {
    "attractions": {"label": "Attraction", "plural": "Attractions"},
    "delicacies": {"label": "Delicacy", "plural": "Delicacies"},
    "festivals": {"label": "Festival", "plural": "Festivals & Celebrations"},
    "myths": {"label": "Myth & Legend", "plural": "Myths & Legends"},
}

# ─────────────────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", places=places)


WIP_SLUGS = set()  # Removed sorsogon from WIP since we now have full data


@app.route("/place/<slug>")
def place(slug):
    if slug not in places:
        return "Place not found", 404
    if slug in WIP_SLUGS:
        return render_template("wip.html", place=places[slug])
    return render_template("place.html", place=places[slug], slug=slug, all_places=places)


@app.route("/detail/<slug>/<section>/<int:idx>")
def detail(slug, section, idx):
    """Individual detail page for an attraction, delicacy, festival, or myth."""
    if slug not in places:
        return "Place not found", 404
    if section not in SECTION_META:
        return "Section not found", 404

    place = places[slug]
    items = place.get(section, [])

    if idx < 0 or idx >= len(items):
        return "Item not found", 404

    item = items[idx]
    meta = SECTION_META[section]

    # Build related items (other items in same section, excluding current)
    related = []
    for i, other in enumerate(items):
        if i != idx:
            related.append({
                "name": other["name"],
                "image": other.get("image"),
                "section": section,
                "key": i,
                "category": meta["label"]
            })

    # Previous / next
    prev_item = None
    next_item = None
    if idx > 0:
        prev_item = {"name": items[idx - 1]["name"], "key": idx - 1}
    if idx < len(items) - 1:
        next_item = {"name": items[idx + 1]["name"], "key": idx + 1}

    return render_template(
        "detail.html",
        place=place,
        slug=slug,
        section=section,
        item=item,
        category_label=meta["label"],
        related=related[:3],
        prev_item=prev_item,
        next_item=next_item,
    )


if __name__ == "__main__":
    app.run(debug=True)
