![image](https://github.com/SamuelEscalante/Workshop-03-ETL/assets/111151068/fbcb1e35-3c5f-4adc-ab81-00409c37d3d5)

Presented by Samuel Escalante Gutierrez - [@SamuelEscalante](https://github.com/SamuelEscalante)

### Tools used

- **Python** <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px">
- **Jupyter Notebooks** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- **PostgreSQL** <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- **SQLAlchemy** <img src="https://quintagroup.com/cms/python/images/sqlalchemy-logo.png/@@images/eca35254-a2db-47a8-850b-2678f7f8bc09.png" alt="SQLalchemy" width="50px" height="21px">
- **Docker** <img src="https://svgl.app/library/docker.svg" alt="Docker" width="50px" height="21px">
- **Apache Kafka**  <img src="https://www.ibm.com/content/dam/adobe-cms/instana/media_logo/Kafka.component.complex-narrative-xl.ts=1690916200661.png/content/adobe-cms/es/es/products/instana/supported-technologies/apache-kafka-observability/_jcr_content/root/table_of_contents/body/content_section_styled/content-section-body/complex_narrative/logoimage" alt="Kafka" width="50px" height="25px">

---
### Workflow
![workshop3-workflow_](https://github.com/SamuelEscalante/Workshop-03-ETL/assets/111151068/f9223940-2b95-456a-bc69-d57f550bd0e0)

---
### About the data

The datasets used in this project were obtained from:

- [🗺️😁 World Happiness Report 2015-2021](https://www.kaggle.com/datasets/mathurinache/world-happiness-report-20152021/data) 

Only dataset from 2015 to 2019

---
### Project organization

![carpetas-workshop3](https://github.com/SamuelEscalante/Workshop-03-ETL/assets/111151068/f781a593-63e1-41e9-936a-2f0ba7a5c3d5)
---

#### Applications :
1. Install Python : [Python Downloads](https://www.python.org/downloads/)
2. Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)
3. Install Docker : [Get Started with Docker](https://www.docker.com/get-started/)

---

### ¿How to run this project?  

1. Clone the project
```bash
  git clone https://github.com/SamuelEscalante/Workshop-03-ETL.git
```

2. Go to the project directory
```bash
  cd Workshop-3-ETL
```

3. In the root of the project, create a `db_settings.json` file, this to set the database credentials
```json
{
  "DIALECT": "The database dialect or type. In this case, it is set to 'postgres' for PostgreSQL.",
  "PGUSER": "Your PostgreSQL database username.",
  "PGPASSWD": "Your PostgreSQL database password.",
  "PGHOST": "The host address or IP where your PostgreSQL database is running.",
  "PGPORT": "The port on which PostgreSQL is listening.",
  "PGDB": "The name of your PostgreSQL database."
}
```

4. Create virtual environment for Python, I used poetry as dependency management and packagin tool.

   - Install poetry
     
   ```bash
     pip install poetry
   ```
   
   - if you want the .venv folder to be created inside the folder, first run this line otherwise skip this step
     
    ```bash
    poetry config virtualenvs.in-project true
    ```

6. Activate the enviroment
```bash
  poetry init
```
Up to this point you would install all the libraries and create the venv , now you have to activate it.
```bash
  poetry shell
```

7.  Create a `.env` file and add this variable:
   
    - WORK_PATH <- Sets the working directory for the application, indicating the base path for performing operations and managing files.

9. __Create your database__, this step is opcional if you are running locally, but if you are in the cloud you must have already your database

10. Start with the notebooks:
- 001_years_EDA_and_model_training

11. Start docker:
    
    - Open docker desktop and open a terminal session and run:
      ```bash
      docker compose up
      ```
    - Open a new terminal session and run this command to enter into docker bash:
      ```bash
      docker exec -it kafka-container bash
      ```
      and then run this commando to create a new topic:
      ```bash
      kafka-topics --bootstrap-server kafka-container:9092 --create --topic world_happiness
      ```
    - Run consumer and producer
   
      **producer.py**
      ```bash
      python producer.py
      ```
      **consumer.py**
      ```bash
      python consumer.py
      ```
      
    - Then go to postgresql and you should have the table 'ml_mnodel'
   
    - Finally go to notebook 002_model_metrics and run it to see the models metrics




## Farewell and Thanks

Thank you for visiting our repository! We hope you find this project useful. If it has been helpful or you simply liked it, consider giving the repository a star! 🌟

We would love to hear your feedback, suggestions, or contributions.

Thanks for your support! 👋
