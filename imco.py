import sys
import re
import os
import argparse
from PIL import Image
from PIL.ImageFilter import ( BLUR, CONTOUR, DETAIL, SMOOTH, SHARPEN )
from tabulate import tabulate

class FileConvert:
	def __init__(self):
		self.image_filter = "-"
		self.file_input_path = "./"
		self.file_outut_path = "./"
		self.converted_files = []

	def __str__(self):
		headers = {
				"file_source" : "SOURCE FILE",
				"converted_file" : "CONVERTED FILE",
				"file_size_source" : " SIZE SOURCE",
				"path" : "PATH TO NEW FILE/S",
				"file_size_converted" : "SIZE CONVERTED FILE",
				"filter": "FILTER"
				}
		return(tabulate(self._converted_files, headers, tablefmt="grid"))

	@property
	def filename_input(self):
		return self._filename_input

	@filename_input.setter
	def filename_input(self, filename_input):
		self._filename_input = filename_input

	@property
	def filename_output(self):
		return self._filename_output

	@filename_output.setter
	def filename_output(self, filename_output):
		self._filename_output = filename_output

	@property
	def file_output_path(self):
		return self._file_output_path

	@file_output_path.setter
	def file_output_path(self, file_output_path):
		self._file_output_path = file_output_path

	@property
	def file_input_path(self):
		return self.file_input_path

	@file_input_path.setter
	def file_input_path(self, file_input_path):
		self._file_input_path = file_input_path

	@property
	def converted_files(self):
		return self._converted_files

	@converted_files.setter
	def converted_files(self, converted_files):
		self._converted_files = converted_files

	@property
	def image_filter(self):
		return self._image_filter

	@image_filter.setter
	def image_filter(self, image_filter):
		self._image_filter = image_filter


	def save_input_filename(self, filename):
		if validate_file(filename) == False:
			sys.exit("Invalid filename")
		self._filename_input = filename


	def save_output_filename(self, extension, name=""):
		if name == "":
			filename,_ = self._filename_input.split(".")
			filename = filename + "." + str(extension)
		else:
			filename = str(name) + "." + str(extension)
		if validate_file(filename) == False:
			sys.exit("Invalid input")
		self._filename_output = filename


	def save_output_path(self, path):
		if validate_path(path) == False:
			sys.exit("Invalid Path.")
		self._file_output_path = path


	def save_input_path(self, path):
		if validate_path(path) == False:
			sys.exit("Invalid Path.")
		self._file_input_path = path


	def image_filters(self, image):
		if self.image_filter == "sharpen":
			image = image.filter(SHARPEN)
		elif self.image_filter == "blur":
			image = image.filter(BLUR)
		elif self.image_filter == "smooth":
			image = image.filter(SMOOTH)
		elif self.image_filter == "contour":
			image = image.filter(CONTOUR)
		elif self.image_filter == "detail":
			image = image.filter(DETAIL)
		elif self.image_filter == "bw":
			image = image.convert("L")


	def convert_and_save_image(self):
		with Image.open(self._file_input_path + self._filename_input) as image:
			self.image_filters(image)
			image.save(self._file_output_path + "" + self._filename_output)
		self._converted_files.append({
			"file_source" : self._filename_input,
			"file_size_source": str((int(os.path.getsize(self._file_input_path + self._filename_input) / 1000))) + " kb",
			"path" : self._file_output_path,
			"converted_file" : self._filename_output,
			"file_size_converted": str((int(os.path.getsize(self._file_output_path + self._filename_output) / 1000))) + " kb",
			"filter" : self._image_filter
		})

	def create_thumbnail(self, size):
		with Image.open(self._file_input_path + self._filename_input) as image:
			self.image_filters(image)
			image.thumbnail(size)
			image.save(self._file_output_path + self._filename_output, "JPEG")
			self._converted_files.append({
				"file_source" : self._filename_input,
				"file_size_source": str((int(os.path.getsize(self._file_input_path + self._filename_input) / 1000))) + " kb",
				"path" : self._file_output_path,
				"converted_file" : self._filename_output,
				"file_size_converted": str((int(os.path.getsize(self._file_output_path + self._filename_output) / 1000))) + " kb",
				"filter" : self._image_filter
			})

	def return_sucess_single_file(self):
		return f"Image successfully converted"

	def save_files(self, filename, file_extension, new_file_name="", img_filter=""):
		self.save_input_filename(filename)
		self.save_output_filename(file_extension, new_file_name)
		if img_filter is not None:
			self._image_filter = img_filter


	def set_and_save_dirs(self, custom_path, file_extension, dir):
		path = "./" + custom_path + file_extension + "/"
		self.save_output_path(path)
		if not os.path.isdir(path):
			os.mkdir(path)
		input_path = "./" + dir
		self.save_input_path(input_path)


file_extentions_img = ["jpg", "jpeg", "png", "gif", "bmp", "webp"]
filter_options = ["blur", "sharpen", "smooth", "detail", "bw"]


def main():
	parser = argparse.ArgumentParser(prog='ImageConverter', description='Easy CLI image converter.')

	parser.usage = "\n\nCONVERT A SINGLE IMAGE:\n-file file.jpg -to webp\nOptional: -dir myfolder/ and/or -name filename\n\nCONVERT MULTIPLE IMAGES FROM A FOLDER:\n-dir myfolder/ -type jpg -to webp\n"

	parser.add_argument("-file", help="filename e.g. helloworld.pdf")
	parser.add_argument("-dir", help="get the whole directory")
	parser.add_argument("-name", help="new filename without extension")
	parser.add_argument("-to", help="file exentions of the file format you want your file convert to", choices=file_extentions_img)
	parser.add_argument("-type", help="file exentions of the file source format", choices=file_extentions_img)
	parser.add_argument("-filter", help="adds a filter to an image", choices=filter_options)
	parser.add_argument("-thumb", help="create thumbnail, width x height", nargs=2, type=int)
	args = parser.parse_args()

	fileConverter = FileConvert()

	if len(sys.argv) == 1:
		parser.print_help()

	'''
	Converts a single image
	'''
	if args.file and args.to and not args.thumb:
		fileConverter.save_files(args.file, args.to, args.name, args.filter)
		if args.dir:
			fileConverter.save_output_path(args.dir)
		else:
			fileConverter.save_output_path("./")
		try:
			fileConverter.convert_and_save_image()
			print(results("🤩 Your file has been sussefully converted.", fileConverter))
		except FileNotFoundError:
			sys.exit("\n😱 Source file coulnd't be found\n")

	if args.file and not args.to:
		sys.exit("\n😰 Missing argument. FileConverter can't convert single files if -to and file exention is missing.\nRestart and add the missing args e.g.'-to webp'\nIf you need help read the docs or the help -h\n")

	'''
	Converts all images with a specific file format from a folder
	'''
	if args.dir and args.type and args.to and not args.file and not args.thumb:
		files = get_all_files_from_folder(args.dir, args.type)
		is_folder_empty(files, args.type, args.dir)
		fileConverter.set_and_save_dirs("_image_converter_", args.to, args.dir)
		print(f"\n😎 FileConverting is running. It just takes a moment.\nYou find your fill in the folder ./{args.dir}.")
		for file in files:
			fileConverter.save_files(file, args.to)
			fileConverter.convert_and_save_image()
		print(results("🤩 Your files have been sussefully converted.", fileConverter))


	if args.file is None and args.thumb is None:
		if (args.dir and args.to) and not args.type:
			sys.exit("\n😰 Missing argument: -to + extension\nFor: Extension of the file you want to convert into.\nExample '-to webp'\n")
		if (args.dir and args.type) and not args.to:
			sys.exit("\n😰 Missing argument: -to + extension\nFor: Type of type of the files your want to use from the folder.\nExample '-type webp'\n")

	'''
	create thumbnail from a single img
	'''
	if args.thumb:
		if not args.file and not args.dir:
			sys.exit("\n😰 Missing argument: -file + filename\nWithout a source file there is nothing I can do for you.\nExample '-file filename.jpg'\n")
		if not args.to:
			sys.exit("\n😰 Missing argument: -to + extension\nPlease provide the file format you want to convert to.\nExample '-to jpg'\n")
		if args.file and args.to:
			size = (args.thumb[0], args.thumb[1])
			'''
			crate file name for thumbnail
			'''
			if not args.name:
				if validate_file(args.file):
					name, _ = args.file.split(".")
					thumbnail_filename = name + "_thumb_" + str(args.thumb[0]) + "x" + str(args.thumb[1])
			else:
				thumbnail_filename = args.name + "_thumb_" + str(args.thumb[0]) + "x" + str(args.thumb[1])
			fileConverter.save_files(args.file, args.to, thumbnail_filename, args.filter)
			if args.dir:
				fileConverter.save_output_path(args.dir)
			else:
				fileConverter.save_output_path("./")
			try:
				fileConverter.create_thumbnail(size)
				print(results("🤩 Your file has been sussefully converted.", fileConverter))
			except FileNotFoundError:
				sys.exit("\n😱 Source file coulnd't be found\n")
		if args.dir and not args.file and not args.type:
			sys.exit("\n😰 Missing argument: -type + extension\nFiletype of the files that you want to select.\nExample '-type jpg'\n")
		if args.dir and not args.file and not args.to:
			sys.exit("\n😰 Missing argument: -to + extension\nFiletype of thumbnail.\nExample '-to jpg'\n")
		if args.dir and not args.file and args.to and args.type:
			'''
			create mutiple thumbnails from a folder
			'''
			files = get_all_files_from_folder(args.dir, args.type)
			is_folder_empty(files, args.type, args.dir)
			size = (args.thumb[0], args.thumb[1])
			fileConverter.set_and_save_dirs("_thumbs_", args.to, args.dir)
			print(f"\n😎 FileConverting is running. It just takes a moment to create your thumbnails.\nYou find your fill in the folder ./{args.dir}.")
			for file in files:
				filename, _ = file.split(".")
				thumbnail_filename = filename + "_thumb_" + str(args.thumb[0]) + "x" + str(args.thumb[1])
				fileConverter.save_files(file, args.to, thumbnail_filename, args.filter)
				fileConverter.create_thumbnail(size)
			print(results("🤩 Your files have been sussefully converted.", fileConverter))


def validate_file(filename):
	try:
		_, extentsion = filename.split(".")
	except ValueError:
		return False
	if re.search(r"^([a-zA-Z_0-9]{2,})\.([a-zA-Z_0-9]{2,})$", filename) and extentsion in file_extentions_img:
		return True
	return False


def validate_path(path):
	if re.search(r"^(\.\./|\./)?([a-zA-Z_0-9]*(/){1})*$", path):
		if os.path.isdir("./" + path) == False:
			os.mkdir("./" + path)
		return True
	return False


def results(error, file_list):
	return f"\n{error}\n\n{file_list}\n"


def get_all_files_from_folder(dir, type):
	files = []
	try:
		for file in os.listdir(dir):
			if file.endswith("." + type):
				files.append(file)
		return files
	except FileNotFoundError:
		sys.exit(" \n😱 Directory does not exist.\n")


def is_folder_empty(file_list, file_type, dir):
	if len(file_list) < 1:
		sys.exit(f"\nFolder seems to be empty. 😱 No files with the extentions .{file_type} found in {dir}\n")
	return True


if __name__ == "__main__":
    main()