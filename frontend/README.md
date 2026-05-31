# Gym AI Chatbot - Frontend

A modern, responsive React-based chat interface for the Gym AI Assistant. Built with React, TypeScript, Vite, and featuring dark/light mode support.

## Features

✨ **Key Features:**
- 💬 Real-time chat interface with message history
- 🔄 Loading animation with thinking bubbles while waiting for responses
- 🌓 Light and Dark mode support with automatic theme detection
- 📱 Fully responsive design (mobile, tablet, desktop)
- 🎨 Beautiful, modern UI with smooth animations
- 🗑️ Clear chat history with confirmation dialog
- ⚡ Fast development with Vite
- 🔌 Connected to FastAPI backend
- ♿ Accessible and keyboard-friendly

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ChatContainer.tsx      # Main chat area
│   │   ├── InputBox.tsx           # Message input field
│   │   ├── LoadingBubbles.tsx     # Thinking animation
│   │   ├── Message.tsx            # Individual message bubble
│   │   └── ThemeToggle.tsx        # Light/Dark mode toggle
│   ├── hooks/
│   │   └── useTheme.ts            # Theme management hook
│   ├── services/
│   │   └── chatbotService.ts      # API communication
│   ├── styles/
│   │   ├── App.css                # Global styles and theme
│   │   ├── ChatContainer.css      # Chat UI styles
│   │   ├── InputBox.css           # Input field styles
│   │   ├── LoadingBubbles.css     # Animation styles
│   │   ├── Message.css            # Message bubble styles
│   │   └── ThemeToggle.css        # Toggle button styles
│   ├── types/
│   │   └── index.ts               # TypeScript interfaces
│   ├── App.tsx                    # Main app component
│   └── main.tsx                   # Entry point
├── .env                           # Environment variables
├── .env.example                   # Environment template
├── .gitignore
├── package.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

## Prerequisites

- Node.js 16+ and npm/yarn
- Backend API running on `http://localhost:8000`

## Installation

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Configure environment variables** (optional):
   - The default `.env` is already configured for `http://localhost:8000`
   - If your backend is on a different URL, update `.env`:
```env
VITE_API_URL=http://your-backend-url:port
```

## Development

### Start Development Server

```bash
npm run dev
```

The app will open at `http://localhost:5173` (Vite's default port).

### Debug with VS Code

Option 1: **Debug Both Frontend and Backend Together**
- Open VS Code
- Go to Run and Debug (Cmd+Shift+D on Mac)
- Select "Full Stack: Backend + Frontend"
- Click the play button

Option 2: **Debug Only Frontend**
- Go to Run and Debug
- Select "Frontend: Vite Dev Server"
- Click the play button

## Build

```bash
npm run build
```

This creates an optimized production build in the `dist/` folder.

## API Integration

The frontend communicates with the backend using the `chatbotService`:

### Endpoints Used:
- **POST** `/chatbot/gemini` - Send a message and get a response
- **GET** `/health/` - Health check (optional)

### Request/Response Format:
```typescript
// Request
{
  "question": "What exercises should I do?"
}

// Response
{
  "answer": "Here's a comprehensive workout plan..."
}
```

## Theme System

The app supports two themes:

- **Light Mode** (default): Clean, bright interface
- **Dark Mode**: Easy on the eyes for low-light environments

Theme preference is automatically saved to localStorage and persists across sessions.

### Theme Variables
All colors are defined as CSS variables in `App.css`:
- `--bg-primary`, `--bg-secondary`: Background colors
- `--text-primary`, `--text-secondary`: Text colors
- `--user-bubble-bg`, `--assistant-bubble-bg`: Chat bubble colors
- And more...

## Component Documentation

### ChatContainer
Displays messages and loading state. Manages auto-scroll and clear chat functionality.

**Props:**
- `messages: Message[]` - Array of chat messages
- `isLoading: boolean` - Whether waiting for response
- `onClearChat: () => void` - Clear chat callback

### InputBox
Text input for sending messages. Supports Enter key to submit.

**Props:**
- `onSendMessage: (message: string) => void` - Send message callback
- `disabled: boolean` - Disable input while loading

### MessageBubble
Displays a single message with timestamp.

**Props:**
- `message: Message` - Message object to display

### LoadingBubbles
Animated thinking bubbles shown while awaiting response.

### ThemeToggle
Button to switch between light and dark modes.

**Props:**
- `theme: 'light' | 'dark'` - Current theme
- `onToggle: () => void` - Toggle callback

## Troubleshooting

### Backend not connecting?
- Ensure backend is running on `http://localhost:8000`
- Check that CORS is enabled on the backend
- Verify the `VITE_API_URL` in `.env`

### Styling issues?
- Clear browser cache (Cmd+Shift+Delete on Mac)
- Hard refresh the page (Cmd+Shift+R on Mac)

### Dark mode not working?
- Check browser localStorage is enabled
- Clear site data and restart

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile: iOS Safari 12+, Chrome Mobile

## Performance

- Vite for fast HMR (Hot Module Replacement)
- Code splitting for optimal bundle size
- Lazy loading of components
- Efficient re-renders with React hooks

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - See main project README

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the backend logs
3. Check browser console for errors (F12)
4. Open an issue in the project repository
