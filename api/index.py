import os
from flask import Flask, render_template
 
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')
static_dir = os.path.join(base_dir, '..', 'static')
 
app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

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
                "image": "/static/images/Bicol/legazpicity.mayonvolcano.jpg"
            },
            {
                "name": "Cagsawa Ruins",
                "desc": "The haunting bell tower of an 18th-century church buried by the 1814 Mayon eruption. A striking reminder of nature's power, with Mayon looming perfectly in the background.",
                "image": "/static/images/Bicol/legazpicity.cagsawaruins.jpg"
            },
            {
                "name": "Sumlang Lake",
                "desc": "A serene crater lake offering bamboo raft rides with unobstructed views of Mayon Volcano. Best experienced at sunrise when the cone reflects off the still water.",
                "image": "/static/images/Bicol/legazpicity.sumlanglake.jpg"
            },
            {
                "name": "Legazpi Boulevard",
                "desc": "A scenic waterfront strip perfect for sunset strolls, street food, and panoramic views of the Albay Gulf with Mayon as the eternal backdrop.",
                "image": "/static/images/Bicol/legazpicity.legazpiboulevard.jpg"
            }
        ],
        "delicacies": [
            {
                "name": "Bicol Express",
                "desc": "The region's most famous dish — strips of pork slow-cooked in coconut milk with an avalanche of labuyo chilis and shrimp paste. Fiery, rich, and utterly addictive.",
                "image": "/static/images/Bicol/legazpicity.bicolexpress.jpg"
            },
            {
                "name": "Pinangat",
                "desc": "Taro leaves stuffed with pork, shrimp, and gata (coconut milk), wrapped and slow-braised until tender. A Bicolano comfort food with deep earthy flavors.",
                "image": "/static/images/Bicol/legazpicity.pinangat.jpg"
            },
            {
                "name": "Pili Candy",
                "desc": "Buttery, caramel-glazed pili nuts — a Bicol exclusive. The pili tree grows only in this region, making these sweet treats the ultimate pasalubong (homecoming gift).",
                "image": "/static/images/Bicol/legazpicity.pilicandy.jpg"
            },
            {
                "name": "Kinunot",
                "desc": "Shredded stingray (pagi) or shark cooked in coconut cream with malunggay leaves and red hot peppers. A bold, unforgettable Bicolano classic.",
                "image": "/static/images/Bicol/legazpicity.kinunot.jpg"
            }
        ],
        "festivals": [
            {
                "name": "Ibalong Festival",
                "month": "August",
                "desc": "Legazpi's grandest celebration honoring the epic Ibalong, the ancient mythological saga of Bicol. Week-long street dancing, elaborate costumes depicting heroes and monsters, and cultural performances fill the city.",
                "image": "/static/images/Bicol/legazpicity.ibalongfestival.jpg"
            },
            {
                "name": "Magayon Festival",
                "month": "May",
                "desc": "A month-long tourism festival celebrating Albay's natural and cultural beauty. Named after the legendary princess Magayon, it features trade fairs, beauty pageants, and pilgrimages around the volcano.",
                "image": "/static/images/Bicol/legazpicity.magayonfestival.jpg"
            }
        ],
        "myths": [
            {
                "name": "The Legend of Magayon",
                "desc": "Princess Daragang Magayon (Beautiful Maiden) was so stunning that two chieftains — Panganoron and Pagtuga — waged war over her. In the battle, she and her beloved Panganoron were slain. From their burial mound grew a great volcano, its perfect cone said to be Magayon's eternal beauty. When it erupts, it is said to be Pagtuga's rage — jealousy burning across centuries.",
                "image": "/static/images/Bicol/legazpicity.legendofmagayon.jpg"
            },
            {
                "name": "The Ibalong Epic",
                "desc": "Bicol's own mythological saga tells of three heroes — Baltog, Handyong, and Bantong — who battled monstrous creatures to tame the wild land of Ibalong (ancient Bicol). From serpents with a thousand heads to giant wild boars, these demigods shaped the land into a place fit for humans.",
                "image": "/static/images/Bicol/legazpicity.ibalongepic.jpg"
            }
        ]
    },
    "naga": {
        "name": "Naga City",
        "province": "Camarines Sur",
        "tagline": "Heart of Bicol",
        "hero_color": "#1a5276",
        "description": "Naga City is the cultural, commercial, and spiritual capital of the Bicol region. Home to the beloved Our Lady of Peñafrancia, it pulses with deep Catholic faith, colonial heritage, and a lively university town energy.",
        "image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1200&q=80",
        "image_hint": "naga-city",
        "attractions": [
            {
                "name": "Basilica Minore of Our Lady of Peñafrancia",
                "desc": "The spiritual heart of Naga and all of Bicol. This grand basilica houses the miraculous image of the Ina (Mother) venerated by millions of devotees every year."
            },
            {
                "name": "Camarines Sur Watersports Complex",
                "desc": "One of Asia's premier cable wakeboarding parks. Whether you're a seasoned boarder or first-timer, the CamSur WakePark offers thrills on its Olympic-standard lake."
            },
            {
                "name": "Naga Cathedral (Naga Metropolitan Cathedral)",
                "desc": "A Spanish-era cathedral dating to the 17th century, standing at the heart of the city. Its austere baroque facade and rich interiors speak to Naga's deep colonial history."
            },
            {
                "name": "Plaza Rizal & Downtown Naga",
                "desc": "The bustling city center filled with heritage buildings, street food vendors, and locals going about their day. The old commercial district retains its warm, provincial charm."
            }
        ],
        "delicacies": [
            {
                "name": "Laing",
                "desc": "Dried taro leaves simmered in thick coconut cream with pork, shrimp, or crab, and spiked with ginger and chili. A slow-cooked masterpiece that deepens in flavor over days.",
                "image": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=600&q=80"
            },
            {
                "name": "Bigg's Diner Burgers",
                "desc": "A beloved Naga institution since 1987. Bigg's is the local fast-food chain that Bicolanos proudly champion — their thick, saucy burgers and palabok are a Naga rite of passage.",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&q=80"
            },
            {
                "name": "Sili Ice Cream",
                "desc": "Arguably Bicol's most adventurous delicacy — chili-infused ice cream. The sweet cream and fiery labuyo create an unforgettable push-pull that captures Bicol's bold culinary spirit.",
                "image": "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=600&q=80"
            },
            {
                "name": "Tinutungang Manok",
                "desc": "Chicken simmered in charred coconut and coconut cream, giving it a smoky, nutty depth. The burnt coconut imparts a uniquely Bicolano complexity to this comforting dish.",
                "image": "https://images.unsplash.com/photo-1598103442097-8b74394b95c3?w=600&q=80"
            }
        ],
        "festivals": [
            {
                "name": "Peñafrancia Festival",
                "month": "September",
                "desc": "The largest Marian festival in Asia. Nine days of novena masses, the iconic fluvial procession along the Naga River, and a sea of millions of barefoot devotees escorting the image of Ina back to the basilica. An overwhelming, deeply moving spectacle.",
                "image": "https://images.unsplash.com/photo-1519750783826-e2420f4d687f?w=600&q=80"
            },
            {
                "name": "Naga City Feast",
                "month": "September",
                "desc": "Coinciding with Peñafrancia, the city erupts with food fairs, concerts, trade expositions, and street parties that showcase the best of Camarines Sur's culture and commerce.",
                "image": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=600&q=80"
            }
        ],
        "myths": [
            {
                "name": "The Miracle of Peñafrancia",
                "desc": "In the early 1700s, a young Spaniard named Miguel Robles de Covarrubias was gravely ill. He promised to bring a replica of the Our Lady of Peñafrancia from Salamanca, Spain, if cured. Upon his miraculous recovery, he kept his vow. The image became renowned for miracles, and the devotion has grown across centuries into the massive festival observed today.",
                "image": "https://images.unsplash.com/photo-1548625149-720754874e8e?w=600&q=80"
            },
            {
                "name": "The Origin of the Bicol River",
                "desc": "Local legend tells that the Bicol River was carved by a giant serpent — the Naga (hence the city's name) — that slithered from the mountains to the sea, its enormous body cutting through the earth to create the great waterway that now sustains the entire region.",
                "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&q=80"
            }
        ]
    },
    "sorsogon": {
        "name": "Sorsogon City",
        "province": "Sorsogon",
        "tagline": "Where Land Meets the Whale Shark",
        "hero_color": "#1e8449",
        "description": "At the southernmost tip of Luzon, Sorsogon is where the Bicol Peninsula meets the sea. Famous for whale shark encounters, natural hot springs, and pristine beaches, it is Bicol's wild, unhurried edge — both ecologically extraordinary and deeply soulful.",
        "image": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=1200&q=80",
        "image_hint": "sorsogon-whale-shark",
        "attractions": [
            {
                "name": "Donsol Whale Shark Interaction",
                "desc": "Swimming alongside butanding (whale sharks) in their natural habitat — no cages, no feeding. Donsol is considered one of the world's best places for ethical whale shark encounters, typically from November to June."
            },
            {
                "name": "Bulusan Volcano Natural Park",
                "desc": "A UNESCO-recognized natural park surrounding the active Bulusan Volcano. Its crater lake, rainforest trails, and lake swimming holes make it a dreamy destination for nature lovers."
            },
            {
                "name": "Barcelona Church and Watchtower",
                "desc": "A beautifully preserved Spanish colonial church and watchtower from the 17th century, built to watch for Moro pirate raids. A stunning piece of living history on the Sorsogon coast."
            },
            {
                "name": "Rizal Beach",
                "desc": "A long stretch of gray-black volcanic sand in Gubat, Sorsogon, known for its consistent surf breaks and dramatic atmosphere. Laid-back, local, and far from the tourist trail."
            }
        ],
        "delicacies": [
            {
                "name": "Butanding Fingers",
                "desc": "Not actual whale shark — just a playful name for deep-fried banana fritters shaped like fingers, a popular local snack named in tribute to Donsol's famous gentle giants.",
                "image": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=600&q=80"
            },
            {
                "name": "Hardinera",
                "desc": "A festive Sorsogon meatloaf baked with pork, chorizo, hard-boiled eggs, bell peppers, and pineapple in a llanera mold. Colorful, hearty, and served at every major celebration.",
                "image": "https://images.unsplash.com/photo-1544025162-d76694265947?w=600&q=80"
            },
            {
                "name": "Pili Tart",
                "desc": "A buttery pastry shell filled with sweetened pili nut paste — think of it as a local egg tart but richer, nuttier, and proudly Bicolano. A must-buy pasalubong from any Sorsogon bakery.",
                "image": "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=600&q=80"
            },
            {
                "name": "Ginataang Puso ng Saging",
                "desc": "Banana blossom braised in coconut milk with pork and chili. A humble, deeply satisfying dish that showcases Bicol's genius for transforming simple ingredients into something extraordinary.",
                "image": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=600&q=80"
            }
        ],
        "festivals": [
            {
                "name": "Kasanggayahan Festival",
                "month": "October",
                "desc": "Sorsogon's founding anniversary celebration featuring street dancing competitions, cultural presentations, agri-trade fairs, and beauty pageants that showcase the province's diverse heritage and natural wonders.",
                "image": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&q=80"
            },
            {
                "name": "Butanding Festival",
                "month": "November",
                "desc": "Held in Donsol to welcome the annual return of the whale sharks. The festival includes coastal clean-ups, marine conservation forums, cultural nights, and the opening of the butanding interaction season.",
                "image": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&q=80"
            }
        ],
        "myths": [
            {
                "name": "The Origin of the Butanding",
                "desc": "In Donsol folklore, the whale sharks were once gentle giants who served as ferrymen for the gods, carrying souls across the great waters between worlds. When the gods departed, the butanding chose to remain in Donsol's warm waters — guardians of the passage, too kind to leave the mortals they had grown to love.",
                "image": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&q=80"
            },
            {
                "name": "The Sleeping Bulusan",
                "desc": "Local legend holds that Bulusan Volcano is not a mountain but a sleeping giant who fell into eternal slumber after a great battle with the sea. When the earth shakes or steam rises from the crater, the elders say he stirs in his sleep, dreaming of the ocean he once fought — and the lover he lost to its depths.",
                "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80"
            }
        ]
    }
}

@app.route("/")
def index():
    return render_template("index.html", places=places)
 
WIP_SLUGS = {'naga', 'sorsogon'}

@app.route("/place/<slug>")
def place(slug):
    if slug not in places:
        return "Place not found", 404
    if slug in WIP_SLUGS:
        return render_template("wip.html", place=places[slug])
    return render_template("place.html", place=places[slug], slug=slug, all_places=places)
 
if __name__ == "__main__":
    app.run(debug=True)
