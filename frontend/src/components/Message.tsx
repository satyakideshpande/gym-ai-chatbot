import React from 'react';
import { Message } from '../types';
import '../styles/Message.css';

interface MessageProps {
  message: Message;
}

export const MessageBubble: React.FC<MessageProps> = ({ message }) => {
  const isUser = message.type === 'user';

  return (
    <div className={`message-container ${isUser ? 'user' : 'assistant'}`}>
      <div className="message-bubble">
        <p>{message.content}</p>
        <span className="message-time">
          {message.timestamp.toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit',
          })}
        </span>
      </div>
    </div>
  );
};
