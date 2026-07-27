// runner.js - fill in the TODOs

class ConfigError extends Error {
    constructor(message) {
        super(message);
        this.name = "ConfigError";
    }
}

function loadThreshold() {
    // TODO 1
    const value = process.env.MAX_ITEMS;

    // TODO 2
    if (!value) {
        throw new ConfigError("MAX_ITEMS is not set.");
    }

    // TODO 3
    return Number(value);
}

async function run(items) {
    const limit = loadThreshold();

    if (items.length > limit) {
        throw new Error(`Too many items: ${items.length} > ${limit}`);
    }

    return items.map(i => i.toUpperCase());
}

const verbose = process.argv.includes("--verbose");

// TODO 6
process.on("unhandledRejection", (err) => {
    if (verbose) {
        console.error(err.stack);
    } else {
        console.error(err.message);
    }
    process.exit(1);
});

// TODO 4
(async () => {
    try {
        const result = await run(["apple", "banana", "orange"]);
        console.log(result);
    } catch (err) {

        // TODO 5
        if (verbose) {
            console.error(err.stack);
        } else {
            console.error(err.message);
        }
    }
})();