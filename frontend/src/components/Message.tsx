import React from 'react';
import { Message } from '../types';
import ReactMarkdown from 'react-markdown';
import '../styles/Message.css';

interface MessageProps {
  message: Message;
}

export const MessageBubble: React.FC<MessageProps> = ({ message }) => {
  const isUser = message.type === 'user';

  return (
    <div className={`message-container ${isUser ? 'user' : 'assistant'}`}>
      <div className="message-bubble">
        <div className="message-content">
          {isUser ? (
            <p>{message.content}</p>
          ) : (
            <ReactMarkdown
              components={{
                p: ({ node, ...props }) => <p {...props} />,
                ul: ({ node, ...props }) => <ul {...props} />,
                ol: ({ node, ...props }) => <ol {...props} />,
                li: ({ node, ...props }) => <li {...props} />,
                strong: ({ node, ...props }) => <strong {...props} />,
                em: ({ node, ...props }) => <em {...props} />,
                code: ({ node, inline, children, ...props }: any) => 
                  inline ? <code {...props}>{children}</code> : <pre><code {...props}>{children}</code></pre>,
                a: ({ node, ...props }) => <a {...props} />,
              }}
            >
              {message.content}
            </ReactMarkdown>
          )}
        </div>
        <span className="message-time">
          {message.timestamp.toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true,
          })}
        </span>
      </div>
    </div>
  );
};
