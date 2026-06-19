# GYM AI Chatbot - Full Stack

A full-stack AI-powered gym assistant built with FastAPI (backend) and React (frontend) powered by Google's Generative AI API. This monorepo contains both backend and frontend code for a complete chatbot solution.

## 🌟 Features

- 🤖 **AI-Powered Responses**: Leverages Google's Gemini model for intelligent responses
- ⚡ **Modern Tech Stack**: FastAPI backend + React frontend with TypeScript
- 💬 **Interactive Chat UI**: Beautiful chat interface with real-time messages
- 🌓 **Light/Dark Mode**: Automatic theme detection with persistent preferences
- 🔄 **Loading States**: Animated thinking bubbles while waiting for responses
- 📱 **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile
- 🔒 **Stateless Architecture**: Scalable design with no session management
- 📚 **Knowledge Base**: Integrated gym-related knowledge base for enhanced responses
- 🧪 **Testing Support**: Includes unit tests for backend reliability

## 📋 Prerequisites

### System Requirements
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Node.js 16+** and npm ([Download](https://nodejs.org/))
- **pip** (usually comes with Python)

### API Requirements
- **Google API Key** (Get from [Google AI Studio](https://aistudio.google.com/apikey))

## 📁 Project Structure

```
gym-ai-chatbot/
├── backend/                    # FastAPI backend service
│   ├── app/                   # FastAPI application code
│   │   ├── api/              # API endpoints (chatbot, health)
│   │   ├── core/             # Configuration files
│   │   ├── schemas/          # Pydantic data models
│   │   ├── services/         # Business logic (LLM service)
│   │   ├── utils/            # Utility functions
│   │   └── main.py           # FastAPI app initialization
│   ├── knowledge_base/        # Gym knowledge data
│   ├── tests/                 # Unit tests
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables (create this)
├── frontend/                   # React frontend application
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── hooks/             # Custom React hooks
│   │   ├── services/          # API service layer
│   │   ├── styles/            # CSS with dark mode
│   │   ├── types/             # TypeScript types
│   │   ├── App.tsx            # Main app component
│   │   └── main.tsx           # Entry point
│   ├── package.json           # Node dependencies
│   ├── vite.config.ts         # Vite configuration
│   ├── tsconfig.json          # TypeScript configuration
│   ├── .env                   # Environment variables
│   └── README.md              # Frontend-specific docs
├── .vscode/
│   ├── launch.json            # VS Code debug configuration
│   └── settings.json          # Workspace settings
├── README.md                  # This file
└── .gitignore
```

## 🚀 Quick Start (Full Stack)

### Option 1: Debug Both Frontend and Backend (Recommended)

1. **Install dependencies:**
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend (from root or frontend folder)
cd frontend
npm install
```

2. **Set up environment variables:**
```bash
# Create .env in backend folder
cd backend
touch .env
```

Add to `backend/.env`:
```env
ENVIRONMENT=development
GOOGLE_API_KEY=your_google_api_key_here
```

3. **Open VS Code and start debugging:**
   - Press `Cmd+Shift+D` (Mac) or `Ctrl+Shift+D` (Windows/Linux)
   - Select "Full Stack: Backend + Frontend" from the dropdown
   - Click the ▶️ (play) button

Both services will start automatically:
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

---

### Option 2: Run Services Separately

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # On macOS/Linux
# or: venv\Scripts\activate  # On Windows
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

---

## 🔧 Backend Setup (Detailed)

### 1. Navigate to Backend

```bash
cd backend
```

### 2. Create Virtual Environment

```bash
# Using venv
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the `backend/` directory:

```env
ENVIRONMENT=development
GOOGLE_API_KEY=your_google_api_key_here
```

**Getting your Google API Key:**
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy the key and paste it into `.env`

> ⚠️ **Security Note**: Never commit `.env` to version control.

### 5. Start Backend Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Server will run at: **http://localhost:8000**

#### Access API Documentation:
- **Swagger UI (Interactive):** http://localhost:8000/docs
- **ReDoc (Alternative):** http://localhost:8000/redoc

---

## 🎨 Frontend Setup (Detailed)

### 1. Navigate to Frontend

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment Variables

Frontend already has `.env` configured for local development:

```env
VITE_API_URL=http://localhost:8000
```

To change the backend URL, edit `.env` in the frontend folder.

### 4. Start Frontend Dev Server

```bash
npm run dev
```

Frontend will run at: **http://localhost:5173**

### 5. Build for Production

```bash
npm run build
```

---

## 📡 API Endpoints

### Health Check
**Endpoint:** `GET /health/`

**Response:**
```json
{
  "status": "healthy"
}
```

### Chat with Gemini Bot
**Endpoint:** `POST /chatbot/gemini`

**Request:**
```json
{
  "question": "What is the yearly membership plan cost ?"
}
```

**Response:**
```json
{
  "answer": "The yearly membership plan costs ......"
}
```

### Example using cURL

```bash
# Chat with bot
curl -X POST http://localhost:8000/chatbot/gemini \
  -H "Content-Type: application/json" \
  -d '{"question": "How often should I work out?"}'
```

---

## 🧪 Testing

### Backend Tests

```bash
cd backend

# Install pytest (if not already installed)
pip install pytest

# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_chatbot.py
```

---

## 🐛 Debugging in VS Code

### Debug Configuration Options

1. **Full Stack (Recommended)**
   - Debugs backend API + frontend simultaneously
   - See both server and browser console output

2. **Backend Only**
   - Python debugger for FastAPI
   - Set breakpoints in Python code

3. **Frontend Only**
   - Node debugger for React
   - Set breakpoints in TypeScript/JavaScript code

### How to Use Debugger

1. Open `.vscode/launch.json` (auto-created)
2. Press `Cmd+Shift+D` or `Ctrl+Shift+D` to open Run and Debug
3. Select your debug configuration
4. Click the ▶️ (play) button or press `F5`
5. Set breakpoints by clicking on line numbers
6. Use the debug controls (step, continue, etc.)

### Setting Breakpoints

**Backend (Python):**
```python
def chat(request: ChatRequest):
    answer = llm_service.get_response(request.question)  # Click here to set breakpoint
    return ChatResponse(answer=answer)
```

**Frontend (TypeScript/React):**
```typescript
const handleSendMessage = (text: string) => {
  const userMessage: Message = {  // Click here to set breakpoint
    id: `msg-${Date.now()}`,
    type: 'user',
    content: text,
    timestamp: new Date(),
  };
  // ...
};
```

---

## 🎨 Features Guide

### Chat Interface
- Type your question in the input box
- Press Enter or click Send
- Messages appear with timestamps
- Loading animation shows while waiting

### Theme Toggle
- Click the ☀️/🌙 icon in top-right
- Automatically saves preference
- Light and dark modes fully supported

### Clear Chat
- Click "🗑️ Clear Chat" button
- Confirms before clearing
- Erases all messages from UI

---

## 🔍 Troubleshooting

### Backend Issues

**Error: "ModuleNotFoundError: No module named 'app'"**
- Solution: Run from backend folder where `app/` exists

**Error: "Google API Key not valid"**
- Solution: Verify `.env` file exists and key is correct

**Error: "Port 8000 already in use"**
- Solution: Use different port or kill process using 8000
```bash
# macOS/Linux: Find and kill process
lsof -i :8000
kill -9 <PID>

# Or use different port
uvicorn app.main:app --reload --port 8001
```

### Frontend Issues

**Error: "Cannot find module 'react'"**
- Solution: Run `npm install` in frontend folder

**Error: "Backend not responding"**
- Verify backend is running on http://localhost:8000
- Check `VITE_API_URL` in `.env`

**Dark mode not working:**
- Clear browser cache (Cmd+Shift+Delete)
- Check localStorage is enabled
- Hard refresh (Cmd+Shift+R)

### Connection Issues

**Frontend can't reach backend:**
1. Ensure backend is running
2. Check backend URL in frontend `.env`
3. Verify CORS is enabled (FastAPI has it by default)
4. Check browser console for error messages

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/guide/)
- [Google Generative AI API](https://ai.google.dev/)

---

## 🤝 Contributing

1. Create a feature branch
2. Commit your changes
3. Push to your branch
4. Create a Pull Request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🆘 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review server logs (backend terminal)
3. Check browser console (F12 in frontend)
4. Open an issue in the repository
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Happy coding! 🚀**
