import React, { useState, useCallback } from 'react';
import { Message } from './types';
import { ChatContainer } from './components/ChatContainer';
import { InputBox } from './components/InputBox';
import { ThemeToggle } from './components/ThemeToggle';
import { useTheme } from './hooks/useTheme';
import { chatbotService } from './services/chatbotService';
import './styles/App.css';

export const App: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [, setError] = useState<string | null>(null);
  const { theme, toggleTheme } = useTheme();

  const handleSendMessage = useCallback(async (text: string) => {
    if (!text.trim()) return;

    // Add user message
    const userMessage: Message = {
      id: `msg-${Date.now()}`,
      type: 'user',
      content: text,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await chatbotService.sendMessage(text);

      const assistantMessage: Message = {
        id: `msg-${Date.now()}-response`,
        type: 'assistant',
        content: response,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to get response';
      setError(errorMessage);

      const errorAssistantMessage: Message = {
        id: `msg-${Date.now()}-error`,
        type: 'assistant',
        content: `Sorry, I encountered an error: ${errorMessage}. Please try again.`,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, errorAssistantMessage]);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const handleClearChat = useCallback(async () => {
    try {
      // Call backend to clear conversation memory
      await chatbotService.clearChat();
      
      // Clear frontend state
      setMessages([]);
      setError(null);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to clear chat';
      setError(errorMessage);
      console.error('Error clearing chat:', errorMessage);
    }
  }, []);

  return (
    <div className="app">
      <div className="app-header">
        <ThemeToggle theme={theme} onToggle={toggleTheme} />
      </div>
      <ChatContainer
        messages={messages}
        isLoading={isLoading}
        onClearChat={handleClearChat}
      />
      <InputBox onSendMessage={handleSendMessage} disabled={isLoading} />
    </div>
  );
};
