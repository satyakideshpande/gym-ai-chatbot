# ⚡ Quick Reference Card

## 🚀 Start Everything (Fastest Way)

```bash
# Terminal 1: Backend
cd backend
python -m uvicorn app.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```

**OR** in VS Code: `Cmd+Shift+D` → Select "Full Stack: Backend + Frontend" → Play ▶️

---

## 🔑 One-Time Setup

```bash
# 1. Backend setup
cd backend
pip install -r requirements.txt
echo "ENVIRONMENT=development" > .env
echo "GOOGLE_API_KEY=your_key_here" >> .env

# 2. Frontend setup
cd frontend
npm install
```

---

## 🌐 URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |
| API Docs (ReDoc) | http://localhost:8000/redoc |

---

## 🎯 What to Test

- [ ] Type question in chat
- [ ] See "Chatbot is thinking" with bouncing bubbles
- [ ] See response appear
- [ ] Click theme toggle (☀️/🌙)
- [ ] Click "🗑️ Clear Chat"

---

## 📁 Important Folders

```
backend/
├── .env              ← Add GOOGLE_API_KEY here!
└── requirements.txt

frontend/
├── .env              ← Already configured
├── src/components/   ← React components
├── src/styles/       ← CSS files (light + dark)
└── package.json
```

---

## 🔧 Common Commands

**Frontend:**
```bash
npm install          # Install dependencies
npm run dev         # Start dev server
npm run build       # Build for production
```

**Backend:**
```bash
pip install -r requirements.txt  # Install deps
python -m uvicorn app.main:app --reload  # Start
```

---

## 🐛 Debug Tips

1. **Set Breakpoint**: Click line number in code
2. **Step Through**: Use F10 or step buttons
3. **Inspect Variable**: Hover over variable name
4. **Console**: View F12 (browser) or terminal (backend)

---

## 🆘 Quick Fixes

| Problem | Fix |
|---------|-----|
| Backend not starting | Verify API key in `.env` |
| Frontend not connecting | Check `VITE_API_URL` in `frontend/.env` |
| Styles not loading | Clear browser cache (Cmd+Shift+Delete) |
| "Thinking" won't end | Check backend terminal for errors |
| Port already in use | Change port in config files |

---

## 📚 Documentation

- **Main README.md** - Full documentation
- **SETUP.md** - Getting started guide
- **FRONTEND_SUMMARY.md** - Complete frontend overview
- **frontend/README.md** - Frontend-specific docs
- **CHANGELOG.md** - What's new

---

## 💡 Key Features

✅ Chat UI with message history
✅ Loading animation (3 bouncing bubbles)
✅ Light & Dark modes
✅ Clear chat history
✅ Responsive design
✅ Connected to backend API
✅ VS Code debugging (both frontend & backend)
✅ Type-safe with TypeScript

---

## 🎨 Customize

**Change Colors**: Edit `frontend/src/styles/App.css`
**Change Port**: Edit `frontend/vite.config.ts`
**Change Backend URL**: Edit `frontend/.env`

---

## 📱 Responsive Breakpoints

- **Mobile**: < 768px (fits portrait)
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

---

## ♻️ Hot Reload

- **Backend**: Auto-reloads on Python file save
- **Frontend**: Auto-reloads on React/CSS file save
- **No browser refresh needed** - Just keep coding!

---

## 🚀 Next Steps

1. ✅ `npm install` (frontend)
2. ✅ Add API key to `backend/.env`
3. ✅ Start backend & frontend
4. ✅ Open http://localhost:5173
5. ✅ Test chat functionality
6. ✅ Explore the code
7. ✅ Customize as needed

---

**Print this card and keep it handy! 📋**

---

*For detailed info, see README.md or SETUP.md*
