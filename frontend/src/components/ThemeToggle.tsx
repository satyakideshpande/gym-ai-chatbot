import React from 'react';
import '../styles/ThemeToggle.css';

interface ThemeToggleProps {
  theme: 'light' | 'dark';
  onToggle: () => void;
}

export const ThemeToggle: React.FC<ThemeToggleProps> = ({ theme, onToggle }) => {
  return (
    <button className="theme-toggle" onClick={onToggle} title="Toggle theme">
      {theme === 'light' ? '🌙' : '☀️'}
    </button>
  );
};
