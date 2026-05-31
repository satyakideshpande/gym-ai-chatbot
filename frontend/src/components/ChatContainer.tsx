import React, { useRef, useEffect, useState } from 'react';
import { Message } from '../types';
import { MessageBubble } from './Message';
import { LoadingBubbles } from './LoadingBubbles';
import '../styles/ChatContainer.css';

interface ChatContainerProps {
  messages: Message[];
  isLoading: boolean;
  onClearChat: () => void;
}

export const ChatContainer: React.FC<ChatContainerProps> = ({
  messages,
  isLoading,
  onClearChat,
}) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [showClearConfirm, setShowClearConfirm] = useState(false);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleClear = () => {
    onClearChat();
    setShowClearConfirm(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>Atenx AI</h1>
        <button
          className="clear-btn"
          onClick={() => setShowClearConfirm(true)}
          disabled={messages.length === 0}
          title="Clear chat history"
        >
          🗑️ Clear Chat
        </button>
      </div>

      {showClearConfirm && (
        <div className="confirmation-dialog">
          <p>Are you sure you want to clear the chat history?</p>
          <div className="confirmation-buttons">
            <button className="confirm-btn" onClick={handleClear}>
              Yes, Clear
            </button>
            <button className="cancel-btn" onClick={() => setShowClearConfirm(false)}>
              Cancel
            </button>
          </div>
        </div>
      )}

      <div className="messages-area">
        {messages.length === 0 && !isLoading && (
          <div className="empty-state">
            <h2>Welcome to Atenx</h2>
            <p>Ask me anything about our gym services!</p>
          </div>
        )}

        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}

        {isLoading && (
          <div className="loading-container">
            <div className="loading-text">
              <p>Chatbot is thinking</p>
              <LoadingBubbles />
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>
    </div>
  );
};
