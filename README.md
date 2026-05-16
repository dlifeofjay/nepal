## Nepal Earthquake Damage Prediction

### Overview
This project predicts the vulnerability of buildings in Nepal to earthquake damage using a machine learning model. It features a Streamlit web app for interactive predictions based on building characteristics.

### Features
- Predicts if a building is likely to be safe or damaged in an earthquake.
- User-friendly interface for inputting building details.
- Real-time predictions using a pre-trained model.
- Key input features: age, foundation, floor/roof type, height, land condition, plan, plinth area, position, superstructure.

### Technologies
- Python, Pandas, NumPy
- Scikit-learn (model training)
- Joblib (model loading)
- Streamlit (web app)

### Installation
1. **Clone the repository:**
    ```
    git clone https://github.com/dlifeofjay/nepal.git
    cd nepal
    ```
2. **(Optional) Create a virtual environment:**
    ```
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```
3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
4. **Run the app:**
    ```
    streamlit run NEPAL_APP.py
    ```

### Usage
- Enter building details in the app.
- Click "Predict" to see if the building is likely to be safe or damaged.

#### Example Input
```python
input_data = {
     'age_building': 10,
     'foundation_type': 'RC',
     'ground_floor_type': 'Brick/Stone',
     'height_ft_pre_eq': 15,
     'land_surface_condition': 'Moderate slope',
     'other_floor_type': 'RCC/RB/RBC',
     'plan_configuration': 'Rectangular',
     'plinth_area_sq_ft': 1200,
     'position': 'Not attached',
     'roof_type': 'RCC/RB/RBC',
     'superstructure': 'cement_mortar_brick'
}
```

### Output
- **Safe:** Building is unlikely to suffer major damage.
- **Damaged:** Building is likely to be affected and may need reinforcement.

### Notes
- The app uses a pre-trained model (`nepal.pkl`).
- Input values must match the model’s expected categories.
- Model performance metrics are available in the training notebook.

### Future Enhancements
- Add map-based risk visualization.
- Integrate seismic zone data.
- Support batch predictions.

1 – Likely to be damaged

0 – Likely to be safe

The model was trained on a dataset containing labeled building data collected in Nepal, focusing on attributes that influence structural stability during seismic activity.

How It Works

The user provides input for building characteristics through dropdowns and sliders.

These inputs are passed to the machine learning model.

The model outputs a binary prediction:

1: The building is likely to be damaged in an earthquake.

0: The building is likely to be safe.

A corresponding message is displayed to the user.

Installation
Step 1: Clone the Repository
git clone https://github.com/dlifeofjay/nepal.git
cd nepal

Step 2: Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

Step 3: Install Required Packages
pip install -r requirements.txt

Step 4: Run the App
streamlit run NEPAL_APP.py

Input Parameters
Feature	Description
Age of Building	Number of years since construction
Foundation Type	Type of foundation material used
Ground Floor Type	Material used for the ground floor
Height (ft)	Height of the building in feet
Land Surface Condition	Terrain condition (flat, moderate, steep)
Other Floor Type	Type of other floors used in the building
Plan Configuration	Shape of the building layout
Plinth Area (sq ft)	Total floor area in square feet
Position	Attachment type with other buildings
Roof Type	Type of roof structure
Superstructure	Material used in the main load-bearing structure
Output

Safe: Building is unlikely to suffer major damage in the event of an earthquake.

Damaged: Building is likely to be affected during an earthquake and may require reinforcement.

Example Usage
# Sample input dictionary
input_data = {
    'age_building': 10,
    'foundation_type': 'RC',
    'ground_floor_type': 'Brick/Stone',
    'height_ft_pre_eq': 15,
    'land_surface_condition': 'Moderate slope',
    'other_floor_type': 'RCC/RB/RBC',
    'plan_configuration': 'Rectangular',
    'plinth_area_sq_ft': 1200,
    'position': 'Not attached',
    'roof_type': 'RCC/RB/RBC',
    'superstructure': 'cement_mortar_brick'
}

Notes

The prediction logic uses a pre-trained model, so no training is performed in real time.

Ensure that the input values match the categories the model was trained on.

The model performance (accuracy, precision, recall) can be found in the training notebook or documentation (if available).

Future Enhancements

Integration of geographical coordinates and seismic zone data

Visualization of risk scores on a map

Addition of uncertainty estimates or confidence intervals

Support for batch predictions via file upload
