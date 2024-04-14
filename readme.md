# Flask example

Using Flask to build a sitemap generator.


### Reference:
- Index page template : [Link](https://codepen.io/soufiane-khalfaoui-hassani/pen/LYpPWda)

- Error page template : [Link](https://codepen.io/ricardpriet/pen/qVZxNo)


- Dockerize Flask APP : [Link](https://medium.com/geekculture/how-to-dockerize-your-flask-application-2d0487ecefb8)


## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────redhat-assessment/
| |────templates/
| | |────index.html
| | |────results.html
| | |────error.html
|──────app.py
|──────requirements.txt
|──────readme.md
|──────Dockerfile
|──────k8s.yaml

```


## Flask Configuration

#### Example

```
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
```
### Configuring From Files

#### Example Usage
 
## Run Flask
### Run flask for develop
```
$ python app.py
```
In flask, Default port is `5000`

### Run with Docker

```
$ docker build -t python-sitemap-generator .

$ docker run -p 5000:5000 --name sitemap-generator python-sitemap-generator 
 
```
### Deployment Setup

```
$ curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.22.0/kind-windows-amd64

$ curl.exe -LO "https://dl.k8s.io/release/v1.29.3/bin/windows/amd64/kubectl.exe"

Copy both the executables to "c:/kubernetes" and set env path for the same 
 
```
**Note:** Since we are using locally build image and note from any public image repository we have to load the image to all nodes in the cluster.

### Deployment

```
$ Kind load docker-image python-sitemap-generator
$ kubectl apply --filename https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
$ kubectl apply -f k8s.yaml
 
```

### Sample URL Tested

```
https://www.redhat.com/en

https://lakshmikrishnanaturals.com/

https://www.markdownguide.org/
 
```
### Backtested with Online sitemap Generators

```
https://octopus.do/sitemap/resource/generator

https://www.mysitemapgenerator.com/

```
