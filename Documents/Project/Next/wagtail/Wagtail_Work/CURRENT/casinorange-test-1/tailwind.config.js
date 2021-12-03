module.exports = {
    mode: "jit",
    purge: [
        "./**/templates/**/*.html",
        "./**/*.py",
        "'!./node_modules",
        "'!./**/node_modules",
        "./static_src/**/*.js",
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
