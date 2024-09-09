import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  // root: resolve(__dirname, 'src'),
  base: './',
  plugins: [react()],
  build: {
    assetsDir: 'static',
  },
  resolve: {
    alias: {
      '~bootstrap': resolve(__dirname, 'node_modules/bootstrap'),
    }
  },
  server: {
    port: 3000,
    cors: true,
    hot: true,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000/",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});