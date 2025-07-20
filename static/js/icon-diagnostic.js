// Icon Diagnostic Script for 75Flow
// This script helps diagnose icon loading issues

console.log('🔍 75Flow Icon Diagnostic Script Loaded');

// Check if Remix Icons CSS is loaded
function checkRemixIconsCSS() {
    const remixLink = document.querySelector('link[href*="remixicon"]');
    if (remixLink) {
        console.log('✅ Remix Icons CSS found:', remixLink.href);
        return true;
    } else {
        console.error('❌ Remix Icons CSS not found!');
        return false;
    }
}

// Check if icons are rendering
function checkIconRendering() {
    const icons = document.querySelectorAll('i[class*="ri-"]');
    console.log(`📊 Found ${icons.length} Remix icons on the page`);
    
    if (icons.length === 0) {
        console.error('❌ No Remix icons found on the page!');
        return false;
    }
    
    // Check if icons are visible
    let visibleIcons = 0;
    let invisibleIcons = 0;
    
    icons.forEach((icon, index) => {
        const rect = icon.getBoundingClientRect();
        const isVisible = rect.width > 0 && rect.height > 0;
        
        if (isVisible) {
            visibleIcons++;
        } else {
            invisibleIcons++;
            console.warn(`⚠️ Icon ${index + 1} (${icon.className}) appears to be invisible`);
        }
    });
    
    console.log(`✅ ${visibleIcons} icons are visible`);
    if (invisibleIcons > 0) {
        console.warn(`⚠️ ${invisibleIcons} icons appear to be invisible`);
    }
    
    return visibleIcons > 0;
}

// Check for CSS conflicts
function checkCSSConflicts() {
    const icons = document.querySelectorAll('i[class*="ri-"]');
    const conflicts = [];
    
    icons.forEach((icon, index) => {
        const styles = window.getComputedStyle(icon);
        
        // Check for problematic CSS properties
        if (styles.display === 'none') {
            conflicts.push(`Icon ${index + 1}: display: none`);
        }
        if (styles.visibility === 'hidden') {
            conflicts.push(`Icon ${index + 1}: visibility: hidden`);
        }
        if (styles.opacity === '0') {
            conflicts.push(`Icon ${index + 1}: opacity: 0`);
        }
        if (styles.fontSize === '0px') {
            conflicts.push(`Icon ${index + 1}: font-size: 0px`);
        }
    });
    
    if (conflicts.length > 0) {
        console.warn('⚠️ Potential CSS conflicts detected:');
        conflicts.forEach(conflict => console.warn(`  - ${conflict}`));
        return false;
    } else {
        console.log('✅ No obvious CSS conflicts detected');
        return true;
    }
}

// Check network connectivity for CDN
function checkCDNConnectivity() {
    const remixLink = document.querySelector('link[href*="remixicon"]');
    if (!remixLink) return false;
    
    fetch(remixLink.href, { method: 'HEAD' })
        .then(response => {
            if (response.ok) {
                console.log('✅ Remix Icons CDN is accessible');
            } else {
                console.error('❌ Remix Icons CDN returned error:', response.status);
            }
        })
        .catch(error => {
            console.error('❌ Cannot access Remix Icons CDN:', error.message);
        });
}

// Run all diagnostics
function runIconDiagnostics() {
    console.log('🚀 Starting icon diagnostics...');
    
    const cssLoaded = checkRemixIconsCSS();
    const iconsRendering = checkIconRendering();
    const noConflicts = checkCSSConflicts();
    
    if (cssLoaded && iconsRendering && noConflicts) {
        console.log('🎉 All icon diagnostics passed! Icons should be working correctly.');
    } else {
        console.error('❌ Icon diagnostics failed. Check the issues above.');
    }
    
    // Check CDN connectivity asynchronously
    checkCDNConnectivity();
}

// Run diagnostics when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runIconDiagnostics);
} else {
    runIconDiagnostics();
}

// Export functions for manual testing
window.iconDiagnostics = {
    run: runIconDiagnostics,
    checkCSS: checkRemixIconsCSS,
    checkRendering: checkIconRendering,
    checkConflicts: checkCSSConflicts,
    checkCDN: checkCDNConnectivity
}; 