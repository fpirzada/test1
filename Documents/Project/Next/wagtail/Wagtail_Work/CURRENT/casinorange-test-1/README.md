# Casinorange project dev notes

## A. Dev setup

### 1. Install Python dependencies:

Python dependencies are split into runtime dependencies (in `requirements.txt`) and
dev/test dependencies (in `requirements-dev.txt`), let's install them first:

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Install Node.js dependencies:

We use `Tailwind` for CSS and `Petit-vue` for JavaScript. You can find the complete frontend setup
in the `./static_src` directory.

In order to start, we need to install Node dependencies, run the following command at the root of the project:

```
npm install
```

### 3. Install pre-commit hooks:

To run code checks before commits, we use pre-commit hooks. When you
start a project, you need to install them at first. Do this by running the following command:

```bash
pre-commit install
```

### 4. Setup environment variables

Copy `.env.sample` to `.env` and fill in `DATABASE_URL` and other missing values.

### 5. Run initial migrations

```
python manage.py migrate
```

## B. Running in development

### 1. Run CSS/JavaScript
To start live CSS/JS compilation, run the following command, while at the root of the project:

```
npm run dev
```

### 2. Start Django Server in Dev mode

```
python manage.py runserver_plus
```

### 3. Run all tasks together
Alternatively, instead of launching steps 1 and step 2 individually, you can run the command:
```
npm run start
```

And it will start the CSS/JS server and a Django dev server in the same terminal.

## C. Test setup
The basic test setup is configured with `Pytest`. The test configuration can be found in the `tox.ini` file.

Run test with:
```
pytest
```

Run coverage report with:
```
pytest --cov
```

## D. Building assets for production

Run the following command to build CSS and JavaScript for production:

```
npm run build
```
