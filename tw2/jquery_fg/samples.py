"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from widgets import MenuWidget

some_items = [
    {'name' : "Breaking News",
        'children' : [ 
            {'name' : "Entertainment",},
            {'name' : "Politics",},
            {'name' : "A&amp;E",},
            {'name' : "Sports", 
                'children' : [ 
                    {'name' : "Baseball",},
                    {'name' : "Basketball",},
                    {'name' : "A really long label would wrap nicely as you can see",},
                    {'name' : "Swimming", 
                        'children' : [ 
                            {'name' : "High School",},
                            {'name' : "College",},
                            {'name' : "Professional", 
                                'children' : [ 
                                    {'name' : "Mens Swimming", 
                                        'children' : [ 
                                            {'name' : "News",},
                                            {'name' : "Events",},
                                            {'name' : "Awards",},
                                            {'name' : "Schedule",},
                                            {'name' : "Team Members",},
                                            {'name' : "Fan Site",},
                                        ]
                                    }, 
                                    {'name' : "Womens Swimming", 
                                        'children' : [ 
                                            {'name' : "News",},
                                            {'name' : "Events",},
                                            {'name' : "Awards",},
                                            {'name' : "Schedule",},
                                            {'name' : "Team Members",},
                                            {'name' : "Fan Site",},
                                        ]
                                    }, 
                                ]
                            }, 
                            {'name' : "Adult Recreational",},
                            {'name' : "Youth Recreational",},
                            {'name' : "Senior Recreational",},
                        ]
                    }, 
                    {'name' : "Tennis",},
                    {'name' : "Ice Skating",},
                    {'name' : "Javascript Programming",},
                    {'name' : "Running",},
                    {'name' : "Walking",},
                ]
            }, 
            {'name' : "Local",},
            {'name' : "Health",},
        ],
    }, 
    {'name' : "Entertainment", 
    'children' : [ 
        {'name' : "Celebrity news",},
        {'name' : "Gossip",},
        {'name' : "Movies",},
        {'name' : "Music", 
        'children' : [ 
            {'name' : "Alternative",},
            {'name' : "Country",},
            {'name' : "Dance",},
            {'name' : "Electronica",},
            {'name' : "Metal",},
            {'name' : "Pop",},
            {'name' : "Rock", 
                'children' : [ 
                    {'name' : "Bands", 
                        'children' : [ 
                            {'name' : "Dokken",},
                        ],
                    }, 
                    {'name' : "Fan Clubs",},
                    {'name' : "Songs",},
                ],
            }, 
        ],
        }, 
        {'name' : "Slide shows",},
        {'name' : "Red carpet",},
    ],
    }, 
    {'name' : "Finance", 
    'children' : [ 
        {'name' : "Personal", 
        'children' : [ 
            {'name' : "Loans",},
            {'name' : "Savings",},
            {'name' : "Mortgage",},
            {'name' : "Debt",},
        ],
        }, 
        {'name' : "Business",},
    ],
    }, 
    {'name' : "Food &#38; Cooking", 
    'children' : [ 
        {'name' : "Breakfast",},
        {'name' : "Lunch",},
        {'name' : "Dinner",},
        {'name' : "Dessert", 
            'children' : [ 
                {'name' : "Dump Cake",},
                {'name' : "Doritos",},
                {'name' : "Both please.",},
            ],
        }, 
    ],
    }, 
    {'name' : "Lifestyle",},
    {'name' : "News",},
    {'name' : "Politics",},
    {'name' : "Sports", 
        'children' : [ 
            {'name' : "Baseball",},
            {'name' : "Basketball",},
            {'name' : "Swimming", 
            'children' : [ 
                {'name' : "High School",},
                {'name' : "College",},
                {'name' : "Professional", 
                'children' : [ 
                    {'name' : "Mens Swimming", 
                    'children' : [ 
                            {'name' : "News",},
                            {'name' : "Events",},
                            {'name' : "Awards",},
                            {'name' : "Schedule",},
                            {'name' : "Team Members",},
                            {'name' : "Fan Site",},
                    ],
                    }, 
                    {'name' : "Womens Swimming", 
                    'children' : [ 
                        {'name' : "News",},
                        {'name' : "Events",},
                        {'name' : "Awards",},
                        {'name' : "Schedule",},
                        {'name' : "Team Members",},
                        {'name' : "Fan Site",},
                    ],
                    },
                ],
                }, 
                {'name' : "Adult Recreational",},
                {'name' : "Youth Recreational",},
                {'name' : "Senior Recreational",},
            ],
            }, 
            {'name' : "Tennis",},
            {'name' : "Ice Skating",},
            {'name' : "Javascript Programming",},
            {'name' : "Running",},
            {'name' : "Walking",},
        ],
        }, 
    ]

class DemoMenuWidget(MenuWidget):
    items = some_items
    options = {
        'crumbDefaultText': ' '
    }

