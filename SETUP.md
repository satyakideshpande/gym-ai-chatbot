# 🚀 Getting Started Guide

This guide will help you get the Gym AI Chatbot full-stack application up and running.

## ⚡ Quick Start (5 minutes)

### Prerequisites Check
Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ and npm installed
- ✅ Google API Key (from https://aistudio.google.com/apikey)

### Step 1: Set Up Backend API Key

```bash
# Navigate to backend folder
cd backend

# Create .env file
touch .env

# Add your Google API key to .env
echo "ENVIRONMENT=development" >> .env
echo "GOOGLE_API_KEY=your_api_key_here" >> .env
```

**Replace `your_api_key_here` with your actual Google API key!**

### Step 2: Install Backend Dependencies

```bash
# Still in backend folder
pip install -r requirements.txt
```

### Step 3: Install Frontend Dependencies

```bash
# Navigate to frontend folder
cd ../frontend

# Install Node packages
npm install
```

### Step 4: Start Both Services

#### Option A: Using VS Code Debugger (Recommended)
1. Open VS Code at the project root
2. Press `Cmd+Shift+D` (macOS) or `Ctrl+Shift+D` (Windows/Linux)
3. Select "Full Stack: Backend + Frontend" from the dropdown
4. Click the play (▶️) button
5. Wait for both services to start
6. Open http://localhost:5173 in your browser

#### Option B: Manual Terminal Setup
**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # macOS/Linux: source venv/bin/activate
# OR Windows: venv\Scripts\activate
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Access the app at: **http://localhost:5173**

---

## 🎯 What to Do Next

### 1. Test the Chat Interface
- Open http://localhost:5173 in your browser
- Type a fitness-related question
- Watch the "Chatbot is thinking" animation
- See the response appear

### 2. Test Dark Mode
- Click the ☀️/🌙 button in top-right
- Switch between light and dark modes
- Notice how the interface adapts

### 3. Test Clear Chat
- Click "🗑️ Clear Chat" button
- Confirm the action
- Watch chat history disappear

### 4. View API Swagger Docs
- Go to http://localhost:8000/docs
- Explore all available endpoints
- Try sending requests directly

### 5. Debug (Optional)
- Set breakpoints in code
- Step through execution
- Inspect variable values

---

## 📁 Project Overview

### Backend (`/backend`)
- **FastAPI** web server on port 8000
- **Google Gemini API** for AI responses
- **Pydantic** for data validation
- Endpoints:
  - `GET /health/` - Health check
  - `POST /chatbot/gemini` - Chat with AI

### Frontend (`/frontend`)
- **React 18** with TypeScript
- **Vite** for fast development
- **CSS Modules** with dark mode
- Features:
  - Chat message UI
  - Loading animations
  - Theme toggle
  - Clear chat history

---

## 🔧 Development Workflow

### Adding Features

#### Backend (Add new endpoint)
1. Create endpoint in `backend/app/api/`
2. Define request/response in `backend/app/schemas/`
3. Test with Swagger UI at `/docs`
4. Backend auto-reloads on save

#### Frontend (Add new component)
1. Create component in `frontend/src/components/`
2. Create styles in `frontend/src/styles/`
3. Import and use in App.tsx
4. Frontend auto-refreshes on save

### Installing New Packages

**Backend:**
```bash
cd backend
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

**Frontend:**
```bash
cd frontend
npm install package-name
npm install package-name --save  # Update package.json
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill process using port
kill -9 <PID>

# Or use different port
python -m uvicorn app.main:app --reload --port 8001
```

### Frontend won't start
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Try again
npm run dev
```

### Backend can't find API key
- Verify `.env` file exists in `backend/` folder
- Check `GOOGLE_API_KEY=` has value
- Never commit `.env` file
- Always use `.env.example` as template

### Frontend can't reach backend
- Ensure backend is running on port 8000
- Check `VITE_API_URL` in `frontend/.env`
- Verify CORS is enabled (default for FastAPI)
- Check browser console for error messages

### Dark mode not working
- Clear browser cache (Cmd+Shift+Delete)
- Clear localStorage: Open DevTools > Application > Storage > localStorage
- Hard refresh (Cmd+Shift+R)

---

## 📚 File Structure Guide

### Important Backend Files
```
backend/
├── app/
│   ├── main.py              # FastAPI setup
│   ├── api/chatbot.py       # Chat endpoints
│   ├── services/llm_service.py  # AI logic
│   └── core/config.py       # Settings
├── knowledge_base/
│   └── planet_fitness.txt    # Gym data
├── .env                     # API keys (create this!)
└── requirements.txt         # Python packages
```

### Important Frontend Files
```
frontend/
├── src/
│   ├── App.tsx              # Main component
│   ├── components/          # React components
│   ├── services/chatbotService.ts  # API calls
│   ├── hooks/useTheme.ts    # Theme management
│   ├── styles/              # CSS files
│   └── types/index.ts       # TypeScript types
├── .env                     # API URL
├── package.json             # Node packages
└── vite.config.ts           # Vite config
```

---

## 🎓 Learning Resources

### For Backend Development
- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Google Generative AI API](https://ai.google.dev/)

### For Frontend Development
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/)
- [CSS Variables Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

### For Full-Stack Development
- [REST API Design](https://restfulapi.net/)
- [VS Code Debugging](https://code.visualstudio.com/docs/editor/debugging)
- [Git Basics](https://git-scm.com/book/en/v2)

---

## 🚀 Production Deployment

### Backend Deployment
```bash
# Use gunicorn for production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### Frontend Deployment
```bash
# Build optimized version
npm run build

# Deploy dist/ folder to static hosting
# (Vercel, Netlify, AWS S3, etc.)
```

---

## 🆘 Getting Help

1. **Check Logs**
   - Backend: Look at terminal where uvicorn is running
   - Frontend: Open DevTools (F12) and check Console

2. **Check Status**
   - Backend health: curl http://localhost:8000/health/
   - Frontend: http://localhost:5173 should load

3. **Check Configuration**
   - Backend: Verify `backend/.env` exists and has API key
   - Frontend: Verify `frontend/.env` has correct backend URL

4. **Common Issues**
   - See README.md "Troubleshooting" section
   - See section above in this file

---

## 📝 Next Steps

1. ✅ Install and start both services
2. ✅ Test the chat interface
3. ✅ Explore the codebase
4. ✅ Try modifying a component
5. ✅ Add a new feature
6. ✅ Deploy to production

---

**Happy coding! 🎉**

For more information, see:
- Main README.md - Full documentation
- frontend/README.md - Frontend-specific docs
- .vscode/launch.json - Debug configurations
