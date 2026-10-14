# ExtinctAPI

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)
![Live API](https://img.shields.io/website?style=flat-square&url=https%3A%2F%2Fextinct-api-1.onrender.com%2Fanimals&label=Live%20API)

A Dockerized Flask REST API providing data on extinct animals and birds, including species names, extinction years, and locations.

Repository: https://github.com/Vimal-Mudalagi/Extinct-API

## Live API

- Endpoint: [https://extinct-api-1.onrender.com/animals](https://extinct-api-1.onrender.com/animals)

Example request:

```bash
curl https://extinct-api-1.onrender.com/animals
```

Example response (truncated):

```json
[
  {
    "name": "Dodo",
    "species": "Raphus cucullatus",
    "extinct_year": 1662,
    "location": "Mauritius"
  }
]
```

## Technologies Used

- Python
- Flask
- Gunicorn
- Docker
- HTML/CSS

## Run Locally (Python)

1. Clone the repository:
   ```bash
   git clone https://github.com/Vimal-Mudalagi/Extinct-API.git
   ```
2. Go to the project directory:
   ```bash
   cd Extinct-API
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the API:
   ```bash
   python extinctapi.py
   ```
5. Open:
   - API: `http://127.0.0.1:5000/animals`
   - Frontend page: `http://127.0.0.1:5000/`

## Run with Docker

The container image exposes port `8000`, and Gunicorn serves the app on `0.0.0.0:8000`.

1. Build the image:
   ```bash
   docker build -t extinct-api .
   ```
2. Run the container:
   ```bash
   docker run --rm -p 8000:8000 extinct-api
   ```
3. Open:
   - API: `http://127.0.0.1:8000/animals`
   - Frontend page: `http://127.0.0.1:8000/`

## Frontend

This project also includes a simple web page that explains the API and provides a button to access the data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgments

This project was created as a learning project to practice Python, Flask REST API development, Gunicorn-based serving, and Docker containerization while exploring information about extinct animals and birds.
