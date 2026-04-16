# Deployment Guide - Titanic Survival Predictor

This guide provides step-by-step instructions to deploy your Titanic Survival Predictor app to GitHub and Vercel.

## Prerequisites
- **GitHub Account**: https://github.com
- **Vercel Account**: https://vercel.com (can sign up with GitHub)
- **Git**: https://git-scm.com
- **Node.js**: https://nodejs.org (v18+)

## Step 1: Push to GitHub

### 1.1 Create a GitHub Repository
1. Go to https://github.com/new
2. Fill in repository details:
   - **Repository name**: `titanic-survival-predictor` (or any name you prefer)
   - **Description**: "Modern Titanic Survival Predictor with data visualizations"
   - **Public/Private**: Choose based on preference
   - Do NOT initialize with README (we already have one)
3. Click **Create repository**

### 1.2 Initialize Git and Push Code
```bash
# Navigate to project directory
cd "c:\Users\ASHISH\Desktop\Titanic Project"

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Titanic Survival Predictor with comprehensive visualizations"

# Rename to main branch
git branch -M main

# Add GitHub remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/titanic-survival-predictor.git

# Push to GitHub
git push -u origin main
```

**Troubleshooting:**
- If git is not found, install it from https://git-scm.com
- If `git push` fails due to authentication, use GitHub Personal Access Token:
  1. Go to https://github.com/settings/tokens
  2. Generate new token with `repo` scope
  3. Use the token as password when prompted

## Step 2: Deploy to Vercel

### Option A: Via Vercel Dashboard (Recommended for Beginners)

1. **Go to Vercel**:
   - Navigate to https://vercel.com/dashboard
   - Sign in with your GitHub account (or create new Vercel account)

2. **Import Project**:
   - Click "Add New..." → "Project"
   - Click "Import Git Repository"
   - Paste your GitHub repository URL: `https://github.com/USERNAME/titanic-survival-predictor`
   - Vercel will automatically detect the project as Next.js

3. **Configure Project**:
   - **Project Name**: `titanic-survival-predictor` (auto-filled)
   - **Framework Preset**: Next.js (should be pre-selected)
   - **Root Directory**: `./` (default)
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `.next` (default)
   - Environment Variables: Leave empty (not needed for this project)

4. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete (~2-3 minutes)
   - You'll get a live URL: `https://your-project-name.vercel.app`

### Option B: Via Vercel CLI (For Advanced Users)

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy**:
   ```bash
   cd "c:\Users\ASHISH\Desktop\Titanic Project"
   vercel
   ```

3. **Follow Prompts**:
   - First time: Link your Vercel account
   - Select scope (your account or team)
   - Confirm project settings
   - Confirm deployment

4. **Done**:
   - Vercel will provide your live URL
   - Example: `https://titanic-predictor-abc123.vercel.app`

## Step 3: Continuous Deployment

Once deployed to Vercel:
- **Every push to `main` branch triggers automatic deployment**
- No additional steps needed
- Vercel handles building and deploying automatically
- Deployments typically complete in 1-2 minutes

### Making Updates:
```bash
# Make changes to your code
# ... edit files ...

# Commit changes
git add .
git commit -m "Add new features"

# Push to GitHub
git push origin main

# Vercel automatically deploys the changes
```

## Step 4: Verify Your Deployment

1. **Check Live URL**:
   - Visit your Vercel deployment URL
   - Fill in passenger details
   - Click "Predict Survival"
   - Verify all charts render correctly

2. **Test Responsiveness**:
   - Open on mobile device
   - Open on tablet
   - Test in different browsers (Chrome, Firefox, Safari)

3. **Check Performance**:
   - Vercel dashboard shows real-time analytics
   - Monitor page load times
   - Check error rates

## Troubleshooting Deployment

### Build Failed
- **Issue**: "npm run build" fails
- **Solution**:
  1. Check Node.js version: `node --version` (should be 18+)
  2. Run locally first: `npm install && npm run build`
  3. Fix any errors, then push to GitHub
  4. Redeploy from Vercel dashboard

### 404 on Live URL
- **Issue**: Page shows 404 error
- **Solution**:
  1. Wait 2-3 minutes for build to complete
  2. Hard refresh browser (Ctrl+Shift+R)
  3. Check Vercel dashboard for build errors

### Port Already in Use (Local Testing)
- **Issue**: Can't run `npm run dev` locally
- **Solution**:
  ```bash
  npm run dev -- --port 3004
  ```

### Git Authentication Failed
- **Issue**: `fatal: could not read Username`
- **Solution**:
  1. Use GitHub Personal Access Token (see Step 1.2)
  2. Or configure SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

## Project Files Included

**Frontend (Deployed to Vercel)**:
- `app/page.tsx` - Main dashboard with all charts
- `app/globals.css` - Complete styling system
- `app/layout.tsx` - Page metadata
- `lib/titanic-model.ts` - Prediction logic
- `package.json`, `next.config.mjs`, `tsconfig.json` - Configuration

**Data**:
- `titani.csv` - Training dataset

**Deployment Config**:
- `.gitignore` - Git ignore patterns
- `.vercelignore` - Vercel build ignore patterns
- `README.md` - Project documentation

**Legacy Files** (Not deployed):
- `titanic_project.py` - Original Python script
- `app.py` - Streamlit version
- `requirements.txt` - Python dependencies
- `venv/` - Python virtual environment

## Vercel Features Included

1. **Automatic HTTPS**: All deployments have SSL certificates
2. **Global CDN**: Content delivered from edge servers worldwide
3. **Automatic Deployments**: Git-based continuous deployment
4. **Environment Variables**: Support for .env.local
5. **Analytics**: Built-in performance monitoring
6. **Preview Deployments**: Test changes before going live
7. **Serverless Functions**: Ready for future backend needs

## Next Steps

After successful deployment:

1. **Share your project**:
   - Share Vercel URL with others
   - Share GitHub repository link

2. **Add features**:
   - Add more visualizations
   - Add export data functionality
   - Add dark/light theme toggle

3. **Monetize** (optional):
   - Add analytics tracking
   - Set up Vercel Pro for advanced features

4. **Monitor**:
   - Check Vercel dashboard regularly
   - Monitor performance metrics
   - Review error logs

## Support

**Common Links**:
- Vercel Docs: https://vercel.com/docs
- Next.js Docs: https://nextjs.org/docs
- GitHub Help: https://docs.github.com

---

**Congratulations!** Your Titanic Survival Predictor is now live on the internet! 🚀
