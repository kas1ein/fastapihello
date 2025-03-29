# Use the official Python 3.12 image from the Docker Hub
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


# Install the dependencies using uv
#RUN uv pip install

# Expose port 8000 for the app
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]