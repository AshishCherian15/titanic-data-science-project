export type PassengerInput = {
  pclass: number;
  sex: "female" | "male";
  age: number;
  sibsp: number;
  parch: number;
  fare: number;
  embarked: "C" | "Q" | "S";
};

const intercept = 5.159335611377201;

const coefficients = {
  pclass: -1.0434160581721281,
  sex: -2.6071632034945122,
  age: -0.037436424320703536,
  fare: 0.002325707836109227,
  familysize: -0.17244320703010857,
  embarked: -0.2320086953602967,
};

const embarkedMap = {
  C: 0,
  Q: 1,
  S: 2,
} as const;

const sexMap = {
  female: 0,
  male: 1,
} as const;

export function predictTitanicSurvival(input: PassengerInput) {
  const familySize = input.sibsp + input.parch + 1;
  const score =
    intercept +
    coefficients.pclass * input.pclass +
    coefficients.sex * sexMap[input.sex] +
    coefficients.age * input.age +
    coefficients.fare * input.fare +
    coefficients.familysize * familySize +
    coefficients.embarked * embarkedMap[input.embarked];

  const probability = 1 / (1 + Math.exp(-score));
  const survived = probability >= 0.5;

  return {
    survived,
    probability,
    familySize,
  };
}
