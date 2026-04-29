{
    "name": "Custom App",
    "version": "1.0",
    "summary": "custom app",
    "description": """
This is a Custom App
========================================

    """,
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/custom_views.xml",
        "views/menu.xml",
        "data/custom_data.xml",
    ],
    "application": True,
    "license": "LGPL-3",
}
