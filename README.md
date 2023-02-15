# py_web_app_demo
py_web_app_demo for cloud deployments

# Local / Dev Set UP

1. create virtual env `virtualenv py_web_app_demo`
2. Activate virtual env `source py_web_app_demo/bin/activate`
3. install requirements `pip install -r requirements.txt`
4. start the app  `uvicorn api.main:app --reload`

URLS
- http://127.0.0.1:8000/docs => Documentation of the API
- http://127.0.0.1:8000 => API end point


# Azure web app Deployment

1. create az web app  `az webapp up --runtime PYTHON:3.8 --sku free --name pyblueocean --logs`
2. az webapp config set --startup-file startup.sh --name <name> --resource-group <rg-name>
3. delete web app `az webapp delete --name MyWebapp --resource-group MyResourceGroup`