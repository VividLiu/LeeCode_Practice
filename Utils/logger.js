class Logger {
    constructor(tag) {
        this.tag = tag === undefined ? 'core' : tag;
        this.debugFlag = true;
    }

    debug(...args) {
        if(this.debugFlag) {
            console.log('[' + this.tag + ']', ...args);
        }            
    }

    setTag(tag) {
        this.tag = tag === undefined ? 'core' : tag;
    }

    setDebugFlag(flag) {
        this.debugFlag = flag;
    }
}

const logger = new Logger();

module.exports = {
    Logger,
    logger
}
