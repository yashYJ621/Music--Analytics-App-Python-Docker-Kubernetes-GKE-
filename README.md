# Music--Analytics-App-Python-Docker-Kubernetes-GKE

```markdown
# Music Analytics App

This project is a music analytics app built using Streamlit, Kubernetes, Docker, and Google Cloud Platform (GCP). Users can input a playlist link, and the app extracts data from the Spotify API using your credentials, storing the extracted data in a PostgreSQL database.

## Local Development Setup

To set up the project for local development, follow these steps:

1. Clone the Repository:
   ```sh
   cd your-repo
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory of the project and add the following variables:
   ```
   SPOTIFY_CLIENT_ID=your-client-id
   SPOTIFY_CLIENT_SECRET=your-client-secret
   ```
   You can use cp .env in your Virtual Environment for better security

4. **Start the Application:**
   ```sh
   streamlit run main_app_entrypoint.py
   ```

5. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8501` to access the app.

## Docker Containerization

To containerize the application using Docker, we follow these steps:

1. **Build the Docker Image:**
   ```sh
   docker build -t music-analytics-app .
   ```

2. **Run the Docker Container:**
   ```sh
   docker run -p 8501:8501 music-analytics-app
   ```

3. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8501` to access the app running inside the Docker container.

## Kubernetes Deployment

To deploy the application to a Kubernetes cluster, we follow these steps:

1. **Set Up Minikube:**
   Follow the Minikube installation guide to install Minikube on your local machine.

2. **Start Minikube:**
   ```sh
   minikube start
   ```

3. **Deploy the Application:**
   ```sh
   kubectl apply -f kubernetes-manifests/
   ```

4. **Access the Application:**
   Use `minikube service <service-name>` to open a browser and view your app.

## Contributing

Feel free to contribute to this project by opening a pull request or an issue. Any feedback or suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

