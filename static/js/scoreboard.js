document.addEventListener('DOMContentLoaded', function() {
    // Enhanced 75-Day Habit Completion Viewer JavaScript
    let currentWeek = 1;
    const totalWeeks = 11; // 75 days = 11 weeks (10 full weeks + 1 partial week)
    let viewMode = 'grid'; // 'grid' or 'list'
    
    // Get habit data from Django template context
    const habitCompletionData = {{ habit_completion_data|safe }};
    const currentUserId = {{ request.user.id }};
    
    // Get current user's habit data
    const userHabitData = habitCompletionData[currentUserId] || {
        habits: [],
        daily_completions: {}
    };
    
    // Initialize the viewer
    updateWeekDisplay();
    updateOverallStats();
    renderCategoryChart();
    renderHabitInsights();
    
    function updateWeekDisplay() {
        const weekStart = (currentWeek - 1) * 7 + 1;
        const weekEnd = Math.min(weekStart + 6, 75);
        
        document.getElementById('currentWeek').textContent = currentWeek;
        document.getElementById('weekStart').textContent = weekStart;
        document.getElementById('weekEnd').textContent = weekEnd;
        
        renderHabitGrid(weekStart, weekEnd);
        updateWeekSummary(weekStart, weekEnd);
        updateWeekProgress(weekStart, weekEnd);
    }
    
    function updateOverallStats() {
        let totalCompletedDays = 0;
        let currentStreak = 0;
        let bestStreak = 0;
        let overallProgress = 0;
        
        for (let day = 1; day <= 75; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            const totalHabits = userHabitData.habits.length;
            const completionPercentage = totalHabits > 0 ? (completedHabits.length / totalHabits) * 100 : 0;
            
            if (completionPercentage >= 80) {
                totalCompletedDays++;
                currentStreak++;
                bestStreak = Math.max(bestStreak, currentStreak);
            } else {
                currentStreak = 0;
            }
            
            overallProgress += completionPercentage;
        }
        
        overallProgress = Math.round(overallProgress / 75);
        
        document.getElementById('totalCompletedDays').textContent = totalCompletedDays;
        document.getElementById('currentStreak').textContent = currentStreak;
        document.getElementById('bestStreak').textContent = bestStreak;
        document.getElementById('overallProgress').textContent = overallProgress + '%';
    }
    
    function renderHabitGrid(weekStart, weekEnd) {
        const gridBody = document.getElementById('habitGrid');
        gridBody.innerHTML = '';
        
        for (let day = weekStart; day <= weekEnd; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            const totalHabits = userHabitData.habits.length;
            const completionPercentage = totalHabits > 0 ? (completedHabits.length / totalHabits) * 100 : 0;
            
            let statusClass = 'pending';
            let statusText = 'Pending';
            let statusIcon = 'ri-time-line';
            
            if (completionPercentage >= 80) {
                statusClass = 'completed';
                statusText = 'Completed';
                statusIcon = 'ri-check-double-line';
            } else if (completionPercentage >= 30) {
                statusClass = 'partial';
                statusText = 'Partial';
                statusIcon = 'ri-check-line';
            }
            
            const row = document.createElement('div');
            row.className = `grid-row ${statusClass}`;
            
            // Group habits by category
            const habitsByCategory = {};
            userHabitData.habits.forEach(habit => {
                if (!habitsByCategory[habit.category]) {
                    habitsByCategory[habit.category] = [];
                }
                habitsByCategory[habit.category].push(habit);
            });
            
            const categoryGroups = Object.entries(habitsByCategory).map(([category, habits]) => {
                const categoryHabits = habits.map(habit => {
                    const isCompleted = completedHabits.find(h => h.id === habit.id);
                    return `<span class="habit-badge ${isCompleted ? 'completed' : 'pending'}">
                        <i class="ri-${isCompleted ? 'check-line' : 'time-line'}"></i>
                        ${habit.name}
                    </span>`;
                }).join('');
                
                return `<div class="category-group">
                    <div class="category-name">
                        <i class="ri-folder-line"></i>${category}
                    </div>
                    <div class="habits-list">${categoryHabits}</div>
                </div>`;
            }).join('');
            
            row.innerHTML = `
                <div class="day-number">Day ${day}</div>
                <div class="habits-categories">${categoryGroups}</div>
                <div class="completion-info">
                    <div class="completion-percentage">${Math.round(completionPercentage)}%</div>
                    <div class="completion-bar">
                        <div class="completion-fill" style="width: ${completionPercentage}%"></div>
                    </div>
                    <div class="completion-text">${completedHabits.length}/${totalHabits} habits</div>
                </div>
                <div class="day-status status-${statusClass}">
                    <i class="${statusIcon}"></i>
                    ${statusText}
                </div>
            `;
            
            gridBody.appendChild(row);
        }
    }
    
    function updateWeekSummary(weekStart, weekEnd) {
        let completedDays = 0;
        let currentStreak = 0;
        let totalCompletion = 0;
        
        for (let day = weekStart; day <= weekEnd; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            const totalHabits = userHabitData.habits.length;
            const completionPercentage = totalHabits > 0 ? (completedHabits.length / totalHabits) * 100 : 0;
            
            if (completionPercentage >= 80) {
                completedDays++;
                currentStreak++;
            } else {
                currentStreak = 0;
            }
            
            totalCompletion += completionPercentage;
        }
        
        const weekProgress = Math.round(totalCompletion / (weekEnd - weekStart + 1));
        
        document.getElementById('weekCompleted').textContent = completedDays;
        document.getElementById('weekStreak').textContent = currentStreak;
        document.getElementById('weekPercentage').textContent = `${weekProgress}%`;
        document.getElementById('weekGoal').textContent = `${completedDays}/${weekEnd - weekStart + 1}`;
    }
    
    function updateWeekProgress(weekStart, weekEnd) {
        let totalCompletion = 0;
        
        for (let day = weekStart; day <= weekEnd; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            const totalHabits = userHabitData.habits.length;
            const completionPercentage = totalHabits > 0 ? (completedHabits.length / totalHabits) * 100 : 0;
            totalCompletion += completionPercentage;
        }
        
        const weekProgress = Math.round(totalCompletion / (weekEnd - weekStart + 1));
        
        const progressBar = document.getElementById('weekProgressBar');
        const progressText = document.getElementById('weekProgressText');
        
        progressBar.style.width = `${weekProgress}%`;
        progressText.textContent = `${weekProgress}% Complete`;
    }
    
    function renderCategoryChart() {
        const chartContainer = document.getElementById('categoryChart');
        
        // Group habits by category and calculate completion rates
        const categoryStats = {};
        userHabitData.habits.forEach(habit => {
            if (!categoryStats[habit.category]) {
                categoryStats[habit.category] = {
                    total: 0,
                    completed: 0,
                    habits: []
                };
            }
            categoryStats[habit.category].total++;
            categoryStats[habit.category].habits.push(habit);
        });
        
        // Calculate completion for current week
        const weekStart = (currentWeek - 1) * 7 + 1;
        const weekEnd = Math.min(weekStart + 6, 75);
        
        for (let day = weekStart; day <= weekEnd; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            Object.keys(categoryStats).forEach(category => {
                const categoryHabits = categoryStats[category].habits;
                const completedInCategory = categoryHabits.filter(habit => 
                    completedHabits.find(h => h.id === habit.id)
                ).length;
                
                if (completedInCategory >= 2) { // 2+ activities per category
                    categoryStats[category].completed++;
                }
            });
        }
        
        const chartHTML = Object.entries(categoryStats).map(([category, stats]) => {
            const percentage = stats.total > 0 ? Math.round((stats.completed / 7) * 100) : 0;
            const categoryIcon = getCategoryIcon(category);
            
            return `<div class="category-chart-item">
                <div class="chart-category-icon">
                    <i class="${categoryIcon}"></i>
                </div>
                <div class="chart-category-info">
                    <div class="chart-category-name">${category}</div>
                    <div class="chart-category-stats">${stats.completed}/7 days completed</div>
                </div>
                <div class="chart-category-progress">
                    <div class="progress">
                        <div class="progress-bar" style="width: ${percentage}%"></div>
                    </div>
                    <small>${percentage}%</small>
                </div>
            </div>`;
        }).join('');
        
        chartContainer.innerHTML = chartHTML || '<p class="text-muted text-center">No category data available</p>';
    }
    
    function renderHabitInsights() {
        const insightsContainer = document.getElementById('habitInsights');
        
        // Calculate insights
        const totalHabits = userHabitData.habits.length;
        const totalDays = 75;
        let totalCompletions = 0;
        let bestDay = 0;
        let bestDayCompletions = 0;
        
        for (let day = 1; day <= totalDays; day++) {
            const completedHabits = userHabitData.daily_completions[day] || [];
            totalCompletions += completedHabits.length;
            
            if (completedHabits.length > bestDayCompletions) {
                bestDayCompletions = completedHabits.length;
                bestDay = day;
            }
        }
        
        const averageCompletions = totalHabits > 0 ? Math.round(totalCompletions / totalDays) : 0;
        const completionRate = totalHabits > 0 ? Math.round((totalCompletions / (totalHabits * totalDays)) * 100) : 0;
        
        const insights = [
            {
                icon: 'ri-target-line',
                title: 'Average Daily Completions',
                description: 'Your typical daily habit completion rate',
                metric: averageCompletions + ' habits'
            },
            {
                icon: 'ri-fire-line',
                title: 'Best Performance Day',
                description: `Day ${bestDay} was your most productive day`,
                metric: bestDayCompletions + ' habits'
            },
            {
                icon: 'ri-percent-line',
                title: 'Overall Completion Rate',
                description: 'Percentage of possible habit completions achieved',
                metric: completionRate + '%'
            },
            {
                icon: 'ri-trending-up-line',
                title: 'Consistency Score',
                description: 'How consistently you complete your habits',
                metric: Math.min(100, Math.round(completionRate * 1.2)) + '%'
            }
        ];
        
        const insightsHTML = insights.map(insight => `
            <div class="col-md-6 col-lg-3 mb-3">
                <div class="insight-card">
                    <div class="insight-icon">
                        <i class="${insight.icon}"></i>
                    </div>
                    <div class="insight-title">${insight.title}</div>
                    <div class="insight-description">${insight.description}</div>
                    <div class="insight-metric">${insight.metric}</div>
                </div>
            </div>
        `).join('');
        
        insightsContainer.innerHTML = insightsHTML;
    }
    
    function getCategoryIcon(category) {
        const iconMap = {
            'Reading': 'ri-book-line',
            'Fitness': 'ri-heart-pulse-line',
            'Nutrition': 'ri-restaurant-line',
            'Wealth': 'ri-money-dollar-circle-line',
            'Spiritual': 'ri-mental-health-line',
            'Fun': 'ri-gamepad-line'
        };
        return iconMap[category] || 'ri-file-list-line';
    }
    
    // Event listeners for navigation
    document.getElementById('prevWeek').addEventListener('click', function() {
        if (currentWeek > 1) {
            currentWeek--;
            updateWeekDisplay();
            renderCategoryChart();
        }
    });
    
    document.getElementById('nextWeek').addEventListener('click', function() {
        if (currentWeek < totalWeeks) {
            currentWeek++;
            updateWeekDisplay();
            renderCategoryChart();
        }
    });
    
    // View mode toggle
    document.getElementById('viewModeToggle').addEventListener('click', function() {
        viewMode = viewMode === 'grid' ? 'list' : 'grid';
        this.innerHTML = viewMode === 'grid' ? 
            '<i class="ri-grid-line me-1"></i>Toggle View' : 
            '<i class="ri-list-check me-1"></i>Toggle View';
        
        // Update grid display based on view mode
        const gridContainer = document.querySelector('.habit-grid-container');
        if (viewMode === 'list') {
            gridContainer.style.gridTemplateColumns = '1fr';
        } else {
            gridContainer.style.gridTemplateColumns = '80px 1fr 120px 100px';
        }
    });
    
    // Export data functionality
    document.getElementById('exportData').addEventListener('click', function() {
        const data = {
            user: currentUserId,
            habits: userHabitData.habits,
            completions: userHabitData.daily_completions,
            week: currentWeek,
            exportDate: new Date().toISOString()
        };
        
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `habit-data-week-${currentWeek}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    // Category Performance Overview Functions
    function showCategoryDetails(categoryName) {
        // This function will show detailed category information
        console.log('Showing details for category:', categoryName);
        // You can implement a modal or redirect to a detailed view
        alert(`Detailed view for ${categoryName} category coming soon!`);
    }

    function compareCategory(categoryName) {
        // This function will show category comparison
        console.log('Comparing category:', categoryName);
        // You can implement a comparison view
        alert(`Comparison view for ${categoryName} category coming soon!`);
    }

    // Initialize category performance overview
    function initializeCategoryOverview() {
        // Add any initialization logic for the category overview
        console.log('Category Performance Overview initialized');
    }

    // Call initialization
