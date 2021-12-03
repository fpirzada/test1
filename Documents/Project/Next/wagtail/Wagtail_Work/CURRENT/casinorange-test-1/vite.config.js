const path = require('path');

export default {
    build: {
        outDir: './static',
        emptyOutDir: true,
        // Vite uses rollup under the hood, here we customize rollup options:
        rollupOptions: {
            // our main entry point file
            input: './static_src/main.js',
            output: {
                entryFileNames: `assets/[name].js`,
                assetFileNames: `assets/[name].[ext]`
            }
        },
        resolve: {
            alias: {
                '@': path.resolve(__dirname, './static_src'),
            }
        }
    }
}
