/**
 * This holds scripts that should be run at the beginning, to start up the project.
 */
import { createApp } from 'petite-vue';

// Removes .no-js class on the <html> element when JavaScript and DOM are ready.
document.addEventListener("DOMContentLoaded", () => document.documentElement.classList.remove("no-js"));

// Bootstraps Petite-Vue:
createApp({
    $delimiters: ['${', '}']
}).mount();
