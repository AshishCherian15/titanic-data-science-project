# Titanic Survival Predictor

A modern, dark-themed Titanic Survival Predictor web app built with Next.js 15 and designed for Vercel deployment.

This project uses a futuristic dashboard layout with glowing blue and green accents, soft shadows, motion effects, and comprehensive data visualization panels. The app runs entirely in the browser, making it perfect for GitHub and Vercel deployment workflows.

## 🎯 Features
- ✅ **Interactive Passenger Input Form** - Enter passenger details (class, gender, age, family size, fare, embarkation port)
- ✅ **Real-time Prediction** - Browser-side Titanic survival prediction using logistic regression
- ✅ **Model Statistics** - Model accuracy (79.89%) and dataset size (891 passengers)
- ✅ **Comprehensive Data Visualizations**:
  - Survival count breakdown (survived vs. did not survive)
  - Survival rate by passenger class (1st/2nd/3rd)
  - Survival rate by gender (female/male)
  - Age distribution with survival analysis (7 age groups)
  - Survival by embarkation port (Southampton/Cherbourg/Queenstown)
  - Family size impact on survival
  - Confusion matrix heatmap for model evaluation
- ✅ **Data Preview Table** - Sample passenger records from the Titanic dataset
- ✅ **Futuristic Dark Theme** - Neon blue/green accents, glassmorphism panels, smooth animations
- ✅ **Responsive Design** - Works on desktop, tablet, and mobile devices

## 📂 Project Structure
```
├── app/
│   ├── page.tsx          # Main dashboard component with all charts
│   ├── globals.css       # Complete styling system (dark theme, animations, chart styles)
│   └── layout.tsx        # Page metadata and Next.js layout wrapper
├── lib/
│   └── titanic-model.ts  # Browser-side logistic regression model
├── package.json          # Node.js dependencies
├── next.config.mjs       # Next.js configuration
├── tsconfig.json         # TypeScript configuration
├── .gitignore            # Git ignore patterns
├── .vercelignore         # Vercel deployment ignore patterns
├── titani.csv            # Titanic training dataset
└── README.md             # This file
```

## 🚀 Quick Start

### Local Development
1. **Install Node.js** (if not already installed) from https://nodejs.org/
2. **Clone or download** this repository
3. **Install dependencies:**
   ```bash
   npm install
   ```
4. **Start the development server:**
   ```bash
   npm run dev
   ```
5. **Open your browser** to the URL shown in the terminal (usually `http://localhost:3002`)

### Production Build
To create an optimized production build:
```bash
npm run build
npm start
```

## 📊 Using the App

### Passenger Input
Fill in the following fields in the left panel:
- **Passenger Class**: Select 1 (First), 2 (Second), or 3 (Third)
- **Sex**: Choose Female or Male
- **Age**: Enter passenger age (0-100 years)
- **Siblings/Spouses**: Number of family members (0-10)
- **Parents/Children**: Number of parents or children (0-10)
- **Fare**: Ticket price (0-600)
- **Embarkation**: Choose S (Southampton), C (Cherbourg), or Q (Queenstown)

### Prediction Result
Click **Predict Survival** to see:
- Whether the passenger **Survived** or **Did Not Survive**
- **Survival Probability** (0-100%)
- **Confidence Level** (High/Medium/Low)
- **Family Size** used by the model

### Data Visualizations
Explore the right panel charts:
- **Survival Count**: Overall distribution of survivors vs. non-survivors
- **By Passenger Class**: Which class had the highest survival rate (1st Class: 63%)
- **By Gender**: Gender's strong impact on survival (Female: 74%, Male: 19%)
- **By Age Group**: Survival rates across different age ranges
- **By Embarkation Port**: Port of embarkation influence on survival
- **By Family Size**: Impact of traveling with family vs. alone
- **Confusion Matrix**: Model performance metrics (TP, TN, FP, FN)

## 🎨 Design System
The UI follows a modern futuristic data dashboard aesthetic:
- **Color Palette**: Dark navy/black backgrounds with cyan and green accents
- **Components**: Glassmorphic panels with backdrop blur and inset glows
- **Animations**: Smooth fade-in entrance effects, hover lift transforms, pulse glows
- **Charts**: Horizontal and vertical bar charts with stacked survival metrics
- **Typography**: Clean sans-serif fonts with proper hierarchy and color contrast

## 💻 Technology Stack
- **Framework**: Next.js 15.5.15 (React 19, TypeScript 5.9)
- **Styling**: Pure CSS3 with custom properties and animations
- **Model**: Browser-side logistic regression (no API calls needed)
- **Deployment**: Optimized for Vercel

## 🌐 Deploy to Vercel

### Option 1: Git-Based Deployment (Recommended)
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial Titanic Survival Predictor"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/titanic-project.git
   git push -u origin main
   ```

2. **Import to Vercel**:
   - Go to https://vercel.com/new
   - Click "Import Git Repository"
   - Paste your GitHub repository URL
   - Select Next.js as the framework
   - Click "Deploy"

### Option 2: Direct Vercel Upload
1. **Download Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

3. **Follow the prompts** to connect your Vercel account and deploy

## ✅ Production Checklist
- ✅ Production build passes: `npm run build`
- ✅ All TypeScript code type-safe
- ✅ No console errors or warnings
- ✅ Responsive design tested on mobile/tablet/desktop
- ✅ All interactive elements functional
- ✅ Charts render correctly
- ✅ Prediction logic verified
- ✅ .gitignore properly configured
- ✅ .vercelignore excludes unnecessary files
- ✅ Ready for GitHub and Vercel deployment

## 📝 Dataset Information
The app uses the famous Titanic dataset containing 891 passenger records:
- **Total Passengers**: 891
- **Survivors**: 342 (38.4%)
- **Non-Survivors**: 549 (61.6%)
- **Classes Represented**: 1st, 2nd, 3rd
- **Embarkation Ports**: Southampton (S), Cherbourg (C), Queenstown (Q)

## 🤖 Model Details
The prediction model uses **Logistic Regression** trained on the Titanic dataset:
- **Accuracy**: 79.89%
- **Features Used**: Passenger class, sex, age, fare, family size, embarkation
- **Execution**: 100% browser-based (no server calls)

## 📄 Files Reference
- [app/page.tsx](app/page.tsx) - Main dashboard React component (400+ lines)
- [app/globals.css](app/globals.css) - Complete styling with animations and chart styles (1000+ lines)
- [lib/titanic-model.ts](lib/titanic-model.ts) - Trained model coefficients and prediction logic
- [titani.csv](titani.csv) - Full Titanic dataset

## 🐛 Troubleshooting

### Port Already in Use
If port 3000/3002 is in use:
```bash
npm run dev -- --port 3003
```

### Module Not Found Error
Clear the cache and rebuild:
```bash
rm -r .next
npm run build
npm run dev
```

### Build Fails
Ensure Node.js version is 18+:
```bash
node --version
```

## 📚 Additional Resources
- [Next.js Documentation](https://nextjs.org/docs)
- [Vercel Documentation](https://vercel.com/docs)
- [React Documentation](https://react.dev)
- [Titanic Dataset](https://www.kaggle.com/c/titanic)

## 📄 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Ready for Production Deployment** ✅ - This project is fully optimized and ready to be pushed to GitHub and deployed on Vercel.
