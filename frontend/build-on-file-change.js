import { exec } from 'child_process'
import path from 'path'

// Custom plugin to run build on file changes
export default function buildOnChangePlugin() {
  return {
    name: 'build-on-vue-change',
    handleHotUpdate({ file }) {
        // console.log(`File changed: ${file}`)
        // console.log('extname: ', path.extname(file))
        if (path.extname(file) === '.vue'){    
            
        exec('npm run build', (error, stdout, stderr) => {
            console.log('running build')
            if (error) {
            console.error(`Build error: ${error}`)
            return
            }
            console.log(`Build output: ${stdout}`)
            if (stderr) {
            console.error(`Build stderr: ${stderr}`)
            }
        })}
    },
  };
}

