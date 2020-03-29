export const navigation = {
  hierarchy: {
    '~': {
      '.': '/',
      events: {
        '.': '/events',
        enigma: {
          '.': '/events/enigma'
        },
        vista: {
          '.': '/events/vista'
        },
        manthan: {
          '.': '/events/manthan'
        },
        linguipedia: {
          '.': '/events/linguipedia'
        },
        perplexed: {
          '.': '/events/perplexed'
        },
        mathmania: {
          '.': '/events/mathmania'
        },
        ctf: {
          '.': '/events/ctf'
        }
      },
      haxplore: {
        '.': '/haxplore'
      },
      dashboard: {
        '.': '/dashboard'
      },
      team: {
        '.': '/team'
      },
      ca: {
        '.': '/ca'
      },
      referrals: {
        '.': '/referral'
      }
    },
    '404': {
      '~': {
        '.': '/'
      }
    }
  },
  getPwdFromCurrent(current) {
    if (!current) return []
    const rawPath = current.split('/')
    rawPath[0] = '~'
    return rawPath.filter((el) => !!el)
  },
  getLinksFromPwd(pwd) {
    let current = null
    const result = []
    pwd.forEach((dir) => {
      if (current) current = current[dir]
      else current = this.hierarchy[dir]
      result.push(current['.'] || '/')
    })
    return result
  },
  getCurrentNav(pwd) {
    let current = null
    let parent = null
    pwd.forEach((dir) => {
      parent = current
      if (current) current = current[dir]
      else current = this.hierarchy[dir]
    })
    if (current) current['..'] = parent
    return current
  },
  listContents(pwd) {
    const possibleNav = this.getCurrentNav(pwd)
    const result = {}
    for (const key in possibleNav) {
      if (possibleNav[key])
        result[key] = possibleNav[key]['.'] || possibleNav['.']
      else result[key] = null
    }
    return result
  },
  getTargetPageUrl(pwd, targetDir) {
    if (['~', '/'].includes(targetDir)) return '/'
    if (['.', './'].includes(targetDir))
      return this.getLinksFromPwd(pwd).splice(-1)[0]
    const backNav = targetDir.match(/^(\.\.)(\/\.\.)*/g)
    if (backNav) {
      pwd = pwd.slice(0, -backNav[0].split('/').length)
      targetDir = targetDir.slice(backNav[0].length)
    }

    if (
      targetDir &&
      targetDir[0] !== '/' &&
      !(['.', '~'].includes(targetDir[0]) && targetDir[1] === '/')
    ) {
      targetDir = `./${targetDir}`
    }

    let currentDir = null
    if (pwd && pwd.length > 0) {
      const hierarchy = this.getCurrentNav(pwd)
      const route = this.getPwdFromCurrent(targetDir)
      if (route.length === 0) {
        return hierarchy['.']
      }
      route.forEach((dir) => {
        if (currentDir) currentDir = currentDir[dir]
        else currentDir = hierarchy[dir]
      })
    }
    if (currentDir) return currentDir['.']
  }
}

export const terminal = {
  history: [],
  getHistory() {
    return this.history
  },
  addToHistory(pwd, status, input, output) {
    this.history.push({ pwd, status, input, output })
  },
  clearHistory() {
    this.history.splice(0, this.history.length)
  }
}
