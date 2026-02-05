from setuptools import setup, find_packages

setup(
    name="ip-checker",                
    version="1.0.0",                  
    description="Pop-up que mostra IP corporativo",  
    author="Rodrigo Stukas",                 
    packages=find_packages(where="src"),  
    package_dir={"": "src"},          
    install_requires=[               
        "psutil"
    ],
    entry_points={                    
        "console_scripts": [
            "ip-checker=main:iniciar_popup"
        ]
    },
)
