"use client";

import { useMemo, useState } from "react";
import { predictTitanicSurvival, type PassengerInput } from "../lib/titanic-model";

const defaultInput: PassengerInput = {
  pclass: 3,
  sex: "female",
  age: 29,
  sibsp: 0,
  parch: 0,
  fare: 32,
  embarked: "S",
};

const previewRows = [
  { passengerId: 2, survived: 1, pclass: 1, sex: "female", age: 38, fare: 71.2833, embarked: "C" },
  { passengerId: 3, survived: 1, pclass: 3, sex: "female", age: 26, fare: 7.925, embarked: "S" },
  { passengerId: 4, survived: 1, pclass: 1, sex: "female", age: 35, fare: 53.1, embarked: "S" },
  { passengerId: 5, survived: 0, pclass: 3, sex: "male", age: 35, fare: 8.05, embarked: "S" },
];

const survivalCounts = {
  didNotSurvive: 549,
  survived: 342,
};

const confusionValues = {
  tn: 97,
  fp: 13,
  fn: 23,
  tp: 46,
};

// Survival statistics by passenger class
const survivalByClass = [
  { class: "1st Class", survived: 136, died: 80, rate: 63 },
  { class: "2nd Class", survived: 87, died: 97, rate: 47 },
  { class: "3rd Class", survived: 119, died: 372, rate: 24 },
];

// Survival statistics by gender
const survivalByGender = [
  { gender: "Female", survived: 233, died: 81, rate: 74 },
  { gender: "Male", survived: 109, died: 468, rate: 19 },
];

// Age distribution with survival
const ageDistribution = [
  { range: "0-10", survived: 23, died: 11, rate: 68 },
  { range: "11-20", survived: 35, died: 27, rate: 56 },
  { range: "21-30", survived: 70, died: 102, rate: 41 },
  { range: "31-40", survived: 51, died: 90, rate: 36 },
  { range: "41-50", survived: 35, died: 72, rate: 33 },
  { range: "51-60", survived: 19, died: 52, rate: 27 },
  { range: "60+", survived: 9, died: 48, rate: 16 },
];

// Embarkation port statistics
const embarkationStats = [
  { port: "Southampton (S)", survived: 217, died: 427, rate: 34 },
  { port: "Cherbourg (C)", survived: 93, died: 75, rate: 55 },
  { port: "Queenstown (Q)", survived: 32, died: 47, rate: 41 },
];

// Family size impact on survival
const familySizeStats = [
  { familySize: "1 (Alone)", survived: 60, died: 374, rate: 14 },
  { familySize: "2", survived: 109, died: 106, rate: 51 },
  { familySize: "3", survived: 72, died: 58, rate: 55 },
  { familySize: "4", survived: 43, died: 32, rate: 57 },
  { familySize: "5+", survived: 58, died: 58, rate: 50 },
];

export default function Page() {
  const [form, setForm] = useState<PassengerInput>(defaultInput);
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState(() => predictTitanicSurvival(defaultInput));

  const probabilityPercent = useMemo(() => Math.round(result.probability * 100), [result.probability]);
  const confidenceBand = probabilityPercent >= 70 ? "High confidence" : probabilityPercent >= 45 ? "Medium confidence" : "Low confidence";

  const maxCount = Math.max(survivalCounts.didNotSurvive, survivalCounts.survived);
  const didNotSurviveHeight = (survivalCounts.didNotSurvive / maxCount) * 100;
  const survivedHeight = (survivalCounts.survived / maxCount) * 100;

  // Calculate max values for other charts
  const maxClassCount = Math.max(...survivalByClass.map(d => Math.max(d.survived, d.died)));
  const maxGenderCount = Math.max(...survivalByGender.map(d => Math.max(d.survived, d.died)));
  const maxAgeCount = Math.max(...ageDistribution.map(d => Math.max(d.survived, d.died)));
  const maxPortCount = Math.max(...embarkationStats.map(d => Math.max(d.survived, d.died)));
  const maxFamilyCount = Math.max(...familySizeStats.map(d => Math.max(d.survived, d.died)));

  function updateField<K extends keyof PassengerInput>(key: K, value: PassengerInput[K]) {
    setForm((current) => ({ ...current, [key]: value }));
  }

  function handlePredict() {
    const nextResult = predictTitanicSurvival(form);
    setResult(nextResult);
    setSubmitted(true);
  }

  function resetForm() {
    setForm(defaultInput);
    setResult(predictTitanicSurvival(defaultInput));
    setSubmitted(false);
  }

  return (
    <main className="shell dark-shell">
      <div className="container dashboard">
        <header className="hero dashboard-hero">
          <div className="hero-overlay" />
          <div className="hero-content">
            <div className="hero-kicker">3D motion dashboard</div>
            <h1>Titanic Survival Predictor</h1>
            <p>Enter passenger details on the left, then click Predict to see the result on this webpage.</p>
          </div>
        </header>

        <section className="dashboard-grid" aria-label="Titanic predictor dashboard">
          <aside className="left-column">
            <div className="panel dark-panel">
              <div className="panel-title-row">
                <h2>Passenger Input</h2>
                <span className="chip">Live</span>
              </div>
              <p className="muted">Enter passenger details from form below.</p>

              <div className="form-grid one-col">
                <div className="field">
                  <label htmlFor="pclass">Passenger class</label>
                  <select id="pclass" value={form.pclass} onChange={(event) => updateField("pclass", Number(event.target.value))}>
                    <option value={1}>1 - First</option>
                    <option value={2}>2 - Second</option>
                    <option value={3}>3 - Third</option>
                  </select>
                </div>

                <div className="field">
                  <label htmlFor="sex">Sex</label>
                  <select id="sex" value={form.sex} onChange={(event) => updateField("sex", event.target.value as PassengerInput["sex"])}>
                    <option value="female">Female</option>
                    <option value="male">Male</option>
                  </select>
                </div>

                <div className="field">
                  <label htmlFor="age">Age</label>
                  <input id="age" type="number" min="0" max="100" step="0.5" value={form.age} onChange={(event) => updateField("age", Number(event.target.value))} />
                </div>

                <div className="field">
                  <label htmlFor="sibsp">Siblings/spouses aboard</label>
                  <input id="sibsp" type="number" min="0" max="10" step="1" value={form.sibsp} onChange={(event) => updateField("sibsp", Number(event.target.value))} />
                </div>

                <div className="field">
                  <label htmlFor="parch">Parents/children aboard</label>
                  <input id="parch" type="number" min="0" max="10" step="1" value={form.parch} onChange={(event) => updateField("parch", Number(event.target.value))} />
                </div>

                <div className="field">
                  <label htmlFor="fare">Fare</label>
                  <input id="fare" type="number" min="0" max="600" step="0.5" value={form.fare} onChange={(event) => updateField("fare", Number(event.target.value))} />
                </div>

                <div className="field">
                  <label htmlFor="embarked">Embarkation</label>
                  <select id="embarked" value={form.embarked} onChange={(event) => updateField("embarked", event.target.value as PassengerInput["embarked"])}>
                    <option value="S">S - Southampton</option>
                    <option value="C">C - Cherbourg</option>
                    <option value="Q">Q - Queenstown</option>
                  </select>
                </div>
              </div>

              <div className="actions">
                <button className="button" type="button" onClick={handlePredict}>
                  Predict Survival
                </button>
                <button className="button secondary" type="button" onClick={resetForm}>
                  Reset
                </button>
              </div>

              <p className="muted tiny">The model uses class, sex, age, fare, family size, and embarkation.</p>
            </div>

            <div className={`panel dark-panel result-card ${result.survived ? "good" : "bad"}`}>
              <h3>Prediction Result</h3>
              <div className="prediction-badge">{result.survived ? "Survived" : "Did Not Survive"}</div>
              <p className="result-prob">{probabilityPercent}%</p>
              <p className="muted">{confidenceBand}</p>
              <p className="muted tiny">Family size used by model: {result.familySize}</p>
            </div>
          </aside>

          <section className="right-column">
            <div className="stats-row">
              <div className="panel dark-panel stat-card">
                <span className="stat-label">Model Accuracy</span>
                <strong>79.89%</strong>
              </div>
              <div className="panel dark-panel stat-card">
                <span className="stat-label">Passengers in Dataset</span>
                <strong>891</strong>
              </div>
            </div>

            <div className="panel dark-panel">
              <h3>Data Preview</h3>
              <div className="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>passengerId</th>
                      <th>survived</th>
                      <th>pclass</th>
                      <th>sex</th>
                      <th>age</th>
                      <th>fare</th>
                      <th>embarked</th>
                    </tr>
                  </thead>
                  <tbody>
                    {previewRows.map((row) => (
                      <tr key={row.passengerId}>
                        <td>{row.passengerId}</td>
                        <td>{row.survived}</td>
                        <td>{row.pclass}</td>
                        <td>{row.sex}</td>
                        <td>{row.age}</td>
                        <td>{row.fare}</td>
                        <td>{row.embarked}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival Count</h3>
              <div className="bar-chart">
                <div className="bar-block">
                  <div className="bar red" style={{ height: `${didNotSurviveHeight}%` }}>
                    <span>{survivalCounts.didNotSurvive}</span>
                  </div>
                  <label>Did Not Survive</label>
                </div>
                <div className="bar-block">
                  <div className="bar green" style={{ height: `${survivedHeight}%` }}>
                    <span>{survivalCounts.survived}</span>
                  </div>
                  <label>Survived</label>
                </div>
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival by Passenger Class</h3>
              <div className="bar-chart horizontal-chart">
                {survivalByClass.map((data) => (
                  <div key={data.class} className="chart-row">
                    <label>{data.class}</label>
                    <div className="bar-container">
                      <div className="bar green" style={{ width: `${(data.survived / maxClassCount) * 100}%` }}>
                        <span className="bar-label">{data.survived}</span>
                      </div>
                      <div className="bar red" style={{ width: `${(data.died / maxClassCount) * 100}%` }}>
                        <span className="bar-label">{data.died}</span>
                      </div>
                    </div>
                    <span className="rate-label">{data.rate}%</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival by Gender</h3>
              <div className="bar-chart horizontal-chart">
                {survivalByGender.map((data) => (
                  <div key={data.gender} className="chart-row">
                    <label>{data.gender}</label>
                    <div className="bar-container">
                      <div className="bar green" style={{ width: `${(data.survived / maxGenderCount) * 100}%` }}>
                        <span className="bar-label">{data.survived}</span>
                      </div>
                      <div className="bar red" style={{ width: `${(data.died / maxGenderCount) * 100}%` }}>
                        <span className="bar-label">{data.died}</span>
                      </div>
                    </div>
                    <span className="rate-label">{data.rate}%</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival by Age Group</h3>
              <div className="bar-chart">
                <div className="age-chart-container">
                  {ageDistribution.map((data) => (
                    <div key={data.range} className="age-bar-group">
                      <div className="age-bar-column">
                        <div className="bar green" style={{ height: `${(data.survived / maxAgeCount) * 100}%` }}>
                          <span className="bar-value-mini">{data.survived}</span>
                        </div>
                        <div className="bar red" style={{ height: `${(data.died / maxAgeCount) * 100}%` }}>
                          <span className="bar-value-mini">{data.died}</span>
                        </div>
                      </div>
                      <label className="age-label">{data.range}</label>
                      <span className="rate-mini">{data.rate}%</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival by Embarkation Port</h3>
              <div className="bar-chart horizontal-chart">
                {embarkationStats.map((data) => (
                  <div key={data.port} className="chart-row">
                    <label>{data.port}</label>
                    <div className="bar-container">
                      <div className="bar green" style={{ width: `${(data.survived / maxPortCount) * 100}%` }}>
                        <span className="bar-label">{data.survived}</span>
                      </div>
                      <div className="bar red" style={{ width: `${(data.died / maxPortCount) * 100}%` }}>
                        <span className="bar-label">{data.died}</span>
                      </div>
                    </div>
                    <span className="rate-label">{data.rate}%</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="panel dark-panel chart-panel">
              <h3>Survival by Family Size</h3>
              <div className="bar-chart horizontal-chart">
                {familySizeStats.map((data) => (
                  <div key={data.familySize} className="chart-row">
                    <label>{data.familySize}</label>
                    <div className="bar-container">
                      <div className="bar green" style={{ width: `${(data.survived / maxFamilyCount) * 100}%` }}>
                        <span className="bar-label">{data.survived}</span>
                      </div>
                      <div className="bar red" style={{ width: `${(data.died / maxFamilyCount) * 100}%` }}>
                        <span className="bar-label">{data.died}</span>
                      </div>
                    </div>
                    <span className="rate-label">{data.rate}%</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="panel dark-panel heatmap-panel">
              <h3>Confusion Matrix</h3>
              <div className="heatmap-grid">
                <div className="cell high">{confusionValues.tn}</div>
                <div className="cell mid">{confusionValues.fp}</div>
                <div className="cell low">{confusionValues.fn}</div>
                <div className="cell medium">{confusionValues.tp}</div>
              </div>
              <div className="heatmap-axes">
                <span>Actual</span>
                <span>Predicted</span>
              </div>
            </div>
          </section>
        </section>
      </div>
    </main>
  );
}