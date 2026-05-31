import React from 'react';
import '../styles/LoadingBubbles.css';

export const LoadingBubbles: React.FC = () => {
  return (
    <div className="loading-bubbles">
      <div className="bubble"></div>
      <div className="bubble"></div>
      <div className="bubble"></div>
    </div>
  );
};
