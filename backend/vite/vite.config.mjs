import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default {
  server: {
    port: 3000,
    strictPort: true,
  },

  resolve: {
    alias: {
      '@': '/src',
    }
  },
  plugins: [react()],
};

