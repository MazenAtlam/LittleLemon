# Little Lemon Restaurant Project

Welcome to the Little Lemon Restaurant Project! This repository is divided into two main sections, each showcasing different implementations for managing the restaurant's operations:

1. **API Section**: Built with Django Rest Framework (DRF) and Djoser for robust API functionalities.
2. **Full Stack Section**: Implemented using plain Django for the backend and Vanilla JavaScript, Bootstrap, CSS, and Notyf for the frontend.

[![Swagger Docs](https://img.shields.io/badge/Swagger-API%20Docs-blue)](https://MazenAtlam.github.io/LittleLemon/)

---

## Project Features

### API Section
- Developed using **Django Rest Framework (DRF)**.
- **Djoser** used for user authentication and management.
- Interactive **Swagger Documentation** available for exploring API endpoints: [API Docs](https://MazenAtlam.github.io/LittleLemon/).

### Full Stack Section
- Backend: Plain Django for server-side logic and rendering.
- Frontend: 
  - **Vanilla JavaScript** for interactivity.
  - **Bootstrap** for responsive design.
  - **CSS** for custom styling.
  - **Notyf** for elegant notifications.

---

## Running the Project with Docker

The project includes a Dockerfile at the root of the repository for easy setup and deployment. Follow these steps to build and run the application:

### Dockerfile
```dockerfile
FROM python:3.10
LABEL maintainer="Ahmed Shehab <a.shehab.biomedeng@gmail.com>"

WORKDIR /littlelemon_booking

COPY Pipfile  .
RUN pip install --upgrade pip \
        && pip install pipenv

RUN pipenv install --skip-lock --system

COPY . .

VOLUME /littlelemon_booking/db

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Steps to Run
1. Build the Docker image:
   ```bash
   docker build -t littlelemon_booking .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 --name littlelemon_booking -v /workspaces/littlelemon_booking/db:/littlelemon_booking/db littlelemon_booking
   ```

3. Access the application:
   - APIs: Visit `http://localhost:8000/api/`.
   - Full Stack Section: Visit `http://localhost:8000/`.

---

## Contributing
We welcome contributions to enhance the functionality and usability of this project. Please submit a pull request or open an issue for suggestions and improvements.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
