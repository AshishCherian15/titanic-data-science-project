## ⚡ QUICK COMMANDS REFERENCE

Use these commands to work with your Titanic Survival Predictor project.

---

## 🚀 DEPLOYMENT COMMANDS

### Push to GitHub
```bash
cd "c:\Users\ASHISH\Desktop\Titanic Project"
git init
git add .
git commit -m "Initial: Titanic Survival Predictor with data visualizations"
git branch -M main
git remote add origin https://github.com/USERNAME/titanic-survival-predictor.git
git push -u origin main
```

### Deploy to Vercel (Option 1: CLI)
```bash
npm install -g vercel
vercel
```

### Deploy to Vercel (Option 2: Dashboard)
```
1. Go to https://vercel.com/new
2. Import Git Repository
3. Paste: https://github.com/USERNAME/titanic-survival-predictor.git
4. Click Deploy
```

---

## 🛠️ DEVELOPMENT COMMANDS

### Install Dependencies
```bash
npm install
```

### Start Development Server
```bash
npm run dev
```

### Build for Production
```bash
npm run build
```

### Run Production Build Locally
```bash
npm run build
npm start
```

### Start on Different Port
```bash
npm run dev -- --port 3004
```

---

## 🧹 MAINTENANCE COMMANDS

### Clear Build Cache
```bash
rm -r .next
npm run build
```

### Update Dependencies
```bash
npm update
```

### Check for Security Issues
```bash
npm audit
```

### Fix Security Issues
```bash
npm audit fix
```

---

## 📊 PROJECT STATISTICS

### File Counts
```
Total Files: 20
Source Code: 4
Configuration: 6
Documentation: 5
Data: 1
Folders: 3 (app, lib, node_modules)
```

### Code Lines
```
React Component: ~500 lines
CSS Styling: ~1000+ lines
Model Code: ~50 lines
Total Code: ~1600 lines
```

### Build Metrics
```
Build Time: 6.1 seconds
Bundle Size: 105 kB
First Load JS: 105 kB
Static Pages: 4
Chunks: 3
```

---

## 📁 FILE REFERENCE

### Source Files
```
app/page.tsx              - Main dashboard component
app/globals.css           - Complete styling system
app/layout.tsx            - Page wrapper and metadata
lib/titanic-model.ts      - Prediction model
```

### Configuration
```
package.json              - Dependencies & scripts
next.config.mjs           - Next.js configuration
tsconfig.json             - TypeScript configuration
.gitignore                - Git ignore patterns
.vercelignore             - Vercel ignore patterns
```

### Documentation
```
README.md                 - Main documentation
DEPLOYMENT.md             - Deployment guide
DEPLOYMENT_CHECKLIST.md   - Quality checklist
CHARTS_GUIDE.md           - Visualization guide
PROJECT_SUMMARY.md        - Completion summary
COMMANDS_REFERENCE.md     - This file
```

### Data & License
```
titani.csv                - Titanic dataset
LICENSE                   - MIT License
```

---

## 🎯 QUICK DEPLOYMENT (5 Minutes)

### Minute 1-2: Git Setup
```bash
cd "c:\Users\ASHISH\Desktop\Titanic Project"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/repo.git
git push -u origin main
```

### Minute 3-4: Create on Vercel
1. Go to https://vercel.com/new
2. Import your GitHub repo
3. Click "Deploy"

### Minute 5: Verify
1. Wait for deployment
2. Open live URL
3. Test the app
4. Share it!

---

## 🔍 TROUBLESHOOTING COMMANDS

### Check Node Version
```bash
node --version
```

### Check npm Version
```bash
npm --version
```

### Clear npm Cache
```bash
npm cache clean --force
```

### Reinstall Dependencies
```bash
rm -r node_modules
npm install
```

### Check Port Usage (Windows)
```bash
netstat -ano | findstr :3000
```

### Kill Process on Port (Windows)
```bash
taskkill /PID 26552 /F
```

---

## 📝 FREQUENTLY USED FILE PATHS

### Project Root
```
c:\Users\ASHISH\Desktop\Titanic Project
```

### Source Code
```
c:\Users\ASHISH\Desktop\Titanic Project\app\
c:\Users\ASHISH\Desktop\Titanic Project\lib\
```

### Configuration
```
c:\Users\ASHISH\Desktop\Titanic Project\package.json
c:\Users\ASHISH\Desktop\Titanic Project\tsconfig.json
```

### Documentation
```
c:\Users\ASHISH\Desktop\Titanic Project\README.md
c:\Users\ASHISH\Desktop\Titanic Project\DEPLOYMENT.md
```

---

## 🌐 USEFUL URLS

### Local Development
```
http://localhost:3000      (default port)
http://localhost:3002      (fallback port)
http://localhost:3003      (if 3000 busy)
```

### GitHub
```
https://github.com/new     (create repo)
https://github.com/username/repo-name  (your repo)
```

### Vercel
```
https://vercel.com/new     (import project)
https://vercel.com/dashboard (view projects)
your-app.vercel.app        (live URL after deploy)
```

### Official Docs
```
https://nextjs.org/docs    (Next.js documentation)
https://vercel.com/docs    (Vercel documentation)
https://react.dev          (React documentation)
```

---

## 📊 CHART DATA REFERENCE

### Survival Statistics
```
Overall: 342 survived, 549 died
By Class: 1st (63%), 2nd (47%), 3rd (24%)
By Gender: Female (74%), Male (19%)
By Age: 0-10 (68%), 60+ (16%)
By Port: Cherbourg (55%), Queenstown (41%), Southampton (34%)
By Family: Size 4 (57%), Size 1 (14%)
```

### Model Metrics
```
Accuracy: 79.89%
True Negatives: 97
False Positives: 13
False Negatives: 23
True Positives: 46
```

---

## ✅ PRE-DEPLOYMENT CHECKLIST

```bash
# Run these before deploying:

# 1. Build check
npm run build

# 2. Verify no errors
npm run dev

# 3. Test locally
# Open http://localhost:3003 in browser

# 4. Git status
git status

# 5. All files staged
git add .

# 6. Ready to commit
git commit -m "Production ready"

# 7. Push to GitHub
git push origin main

# 8. Deploy to Vercel
# Go to vercel.com/new and import
```

---

## 🎓 LEARNING RESOURCES

### React & Next.js
- Official React docs: https://react.dev
- Next.js tutorials: https://nextjs.org/learn
- Full Stack Course: https://www.theodinproject.com

### Web Development
- MDN Web Docs: https://developer.mozilla.org
- CSS-Tricks: https://css-tricks.com
- JavaScript.info: https://javascript.info

### Deployment
- Vercel deployment guide: https://vercel.com/docs/deployments
- Git basics: https://git-scm.com/book/en/v2
- GitHub guides: https://guides.github.com

---

## 💡 PRO TIPS

1. **Always commit before major changes**
   ```bash
   git add .
   git commit -m "Descriptive message"
   ```

2. **Check build before pushing**
   ```bash
   npm run build
   ```

3. **Test on multiple screen sizes**
   - Use browser dev tools (F12)
   - Resize window
   - Test on phone

4. **Monitor Vercel deployments**
   - Watch deployment status
   - Check build logs
   - Monitor performance

5. **Keep dependencies updated**
   ```bash
   npm update
   npm audit
   ```

---

## 🚀 NEXT STEPS

1. ✅ Run `npm run build` to verify build
2. ✅ Run `npm run dev` to test locally
3. ✅ Push to GitHub using git commands
4. ✅ Deploy to Vercel
5. ✅ Share live URL
6. ✅ Monitor performance
7. ✅ Celebrate! 🎉

---

**Last Updated**: April 16, 2026  
**Project**: Titanic Survival Predictor  
**Status**: ✅ Ready for Deployment
