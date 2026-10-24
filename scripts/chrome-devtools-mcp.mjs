// Starts the Chrome DevTools MCP server for Claude Code (.mcp.json runs this).
//
// On a computer it uses the installed Chrome. In a Claude Code cloud session
// there is no Chrome, so it points the server at the pre-installed Chromium.
// The cloud container runs as root, where Chrome only starts without its
// sandbox; the container is already isolated, and on a computer the sandbox
// stays on. Headless and isolated, so it never touches a real browser profile.
import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';

const VERSION = '1.10.1';
const CLOUD_CHROMIUM = '/opt/pw-browsers/chromium';

const args = ['-y', `chrome-devtools-mcp@${VERSION}`, '--headless', '--isolated', '--no-usage-statistics'];
if (existsSync(CLOUD_CHROMIUM)) {
  args.push('--executablePath', CLOUD_CHROMIUM);
  if (process.getuid?.() === 0) args.push('--chromeArg=--no-sandbox');
}

const child = spawn('npx', args, { stdio: 'inherit', shell: process.platform === 'win32' });
child.on('exit', (code) => process.exit(code ?? 0));
