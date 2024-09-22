export default function prependStaticPlugin() {
    return {
      name: 'prepend-static',
      transformIndexHtml(html) {
        // Prepend '/static/' to src and href attributes in script and link tags, and url() in CSS
        return html.replace(
          /(src|href)=["'](?!\/static\/)(\.?\/assets\/[^"']+)["']/g,
          '$1="/static$2"'
        )
      }
    }
  }
