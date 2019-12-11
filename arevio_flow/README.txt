Instructions for Arevio-Flow

REQUIREMENTS: Python 3, node.js and Arevio

PART 1 - DJANGO BACKEND
---------------------------------
- Clone the repo and cd into it.
- python3 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- cd arevio_flow
- python3 manage.py migrate
- python3 manage.py createsuperuser
- python3 manage.py runserver

PART 2 - VUE.JS FRONTEND
---------------------------------
- Open a new terminal
- cd path_to_repo/arevio_flow/frontend
- npm install
- npm run serve

PART 3 - OPEN IN THE BROWSER
---------------------------------
- Go to localhost:[port of django server]

PART 4 - ADDING TAXONOMIES
---------------------------------
- In the Django admin site > Taxonomies, click ADD TAXONOMY.
- Choose a name and an empty XBRL template file (You can find some in path_to_repo/arevio_flow/xbrl_templates).
- For ArelleCmdLine options here are some examples:

Solvency 2.3.0 QRS
------------------
--packages "%ARELLE_HOME%/taxonomies/xbrl/www.xbrl.org.zip|%ARELLE_HOME%/taxonomies/eurofiling/www.eurofiling.info.zip|%ARELLE_HOME%/taxonomies/solvency/2.0.1/EIOPA_SolvencyII_XBRL_Taxonomy_2.0.1.zip|%ARELLE_HOME%/taxonomies/solvency/2.1.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.1.0.zip|%ARELLE_HOME%/taxonomies/solvency/2.2.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.2.0Hotfix.zip|%ARELLE_HOME%/taxonomies/solvency/2.3.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.3.0_Hotfix.zip" --plugins="%ARELLE_HOME%/plugin/acsone/acsoneExtensions.py|%ARELLE_HOME%/plugin/validate/EBA"

Solvency 2.4.0 QRS
------------------
-v --formulaUnsatisfiedAsserError --logFile=testlog.xml --logLevel=warning --internetConnectivity=offline --disclosureSystem=eiopa --plugins="%ARELLE_HOME%/plugin/acsone/acsoneExtensions.py|%ARELLE_HOME%/plugin/validate/EBA" --packages "%ARELLE_HOME%/taxonomies/xbrl/www.xbrl.org.zip|%ARELLE_HOME%/taxonomies/eurofiling/www.eurofiling.info.zip|%ARELLE_HOME%/taxonomies/solvency/2.0.1/EIOPA_SolvencyII_XBRL_Taxonomy_2.0.1.zip|%ARELLE_HOME%/taxonomies/solvency/2.1.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.1.0.zip|%ARELLE_HOME%/taxonomies/solvency/2.2.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.2.0Hotfix.zip|%ARELLE_HOME%/taxonomies/solvency/2.3.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.3.0_Hotfix.zip|%ARELLE_HOME%/taxonomies/solvency/2.4.0/EIOPA_SolvencyII_XBRL_Taxonomy_2.4.0_Hotfix.zip"
