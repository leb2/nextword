/* Run this command to install
npm install --save-dev gulp gulp-autoprefixer gulp-sass gulp-rename gulp-minify-css
*/

var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');
var sass = require('gulp-sass');

var sassDir = './static/sass/**/*.scss';

gulp.task('sass', function() {
    return gulp.src(sassDir)
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(minifyCss())
        .pipe(rename(function(path) {
            path.basename += '.min'
        }))
        .pipe(gulp.dest('./static/stylesheets'));
});

gulp.task('watch', function() {
    gulp.watch(sassDir, ['sass']);
});

gulp.task('default', ['build']);
